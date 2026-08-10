// Build the paper .docx from the constrained-markdown source.
const fs = require('fs');
const path = require('path');
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType,
  Table, TableRow, TableCell, WidthType, BorderStyle, ShadingType, LevelFormat,
} = require('docx');

const SRC = process.argv[2];
const OUT = process.argv[3];
const lines = fs.readFileSync(SRC, 'utf8').split('\n');

const MONO = 'Courier New';
const TABLE_WIDTH = 9000; // DXA inside A4 with 1" margins

function inline(text, extra = {}) {
  const runs = [];
  const re = /(\*\*([^*]+)\*\*)|(\*([^*]+)\*)|(`([^`]+)`)/g;
  let last = 0, m;
  while ((m = re.exec(text))) {
    if (m.index > last) runs.push(new TextRun({ text: text.slice(last, m.index), ...extra }));
    if (m[2] !== undefined) runs.push(new TextRun({ text: m[2], bold: true, ...extra }));
    else if (m[4] !== undefined) runs.push(new TextRun({ text: m[4], italics: true, ...extra }));
    else if (m[6] !== undefined) runs.push(new TextRun({ text: m[6], font: MONO, size: 20, ...extra }));
    last = m.index + m[0].length;
  }
  if (last < text.length) runs.push(new TextRun({ text: text.slice(last), ...extra }));
  return runs.length ? runs : [new TextRun({ text: text, ...extra })];
}

const children = [];
let numInstance = 0;       // restart ordered lists
let inNumList = false;

function flushListState() { inNumList = false; }

function tableFrom(rows) {
  // rows: array of arrays of cell strings; first row = header
  const nCols = Math.max(...rows.map(r => r.length));
  const maxLen = Array(nCols).fill(4);
  rows.forEach(r => r.forEach((c, i) => { maxLen[i] = Math.max(maxLen[i], Math.min(c.length, 60)); }));
  const totalLen = maxLen.reduce((a, b) => a + b, 0);
  const widths = maxLen.map(l => Math.max(700, Math.round(TABLE_WIDTH * l / totalLen)));
  const diff = TABLE_WIDTH - widths.reduce((a, b) => a + b, 0);
  widths[widths.length - 1] += diff;

  const border = { style: BorderStyle.SINGLE, size: 4, color: '999999' };
  return new Table({
    width: { size: TABLE_WIDTH, type: WidthType.DXA },
    columnWidths: widths,
    borders: { top: border, bottom: border, left: border, right: border, insideHorizontal: border, insideVertical: border },
    margins: { top: 60, bottom: 60, left: 100, right: 100 },
    rows: rows.map((r, ri) => new TableRow({
      tableHeader: ri === 0,
      children: widths.map((w, ci) => new TableCell({
        width: { size: w, type: WidthType.DXA },
        shading: ri === 0 ? { type: ShadingType.CLEAR, color: 'auto', fill: 'E8E8E8' } : undefined,
        children: [new Paragraph({
          spacing: { after: 0, line: 240 },
          children: inline(r[ci] || '', { size: 19, bold: ri === 0 ? true : undefined }),
        })],
      })),
    })),
  });
}

let i = 0;
while (i < lines.length) {
  const raw = lines[i];
  const line = raw.replace(/\s+$/, '');

  if (line.startsWith('%TITLE ')) {
    children.push(new Paragraph({ heading: HeadingLevel.TITLE, alignment: AlignmentType.CENTER, children: inline(line.slice(7)) }));
    i++; flushListState(); continue;
  }
  if (line.startsWith('%AUTHOR ')) {
    children.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 60 }, children: inline(line.slice(8), { size: 22 }) }));
    i++; flushListState(); continue;
  }
  if (line.startsWith('%DATE ')) {
    children.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 240 }, children: inline(line.slice(6), { size: 20, italics: true, color: '555555' }) }));
    i++; flushListState(); continue;
  }

  if (line.startsWith('#### ')) { children.push(new Paragraph({ heading: HeadingLevel.HEADING_3, children: inline(line.slice(5)) })); i++; flushListState(); continue; }
  if (line.startsWith('### '))  { children.push(new Paragraph({ heading: HeadingLevel.HEADING_2, children: inline(line.slice(4)) })); i++; flushListState(); continue; }
  if (line.startsWith('## '))   { children.push(new Paragraph({ heading: HeadingLevel.HEADING_1, children: inline(line.slice(3)) })); i++; flushListState(); continue; }

  if (line.startsWith('```')) {
    i++;
    const code = [];
    while (i < lines.length && !lines[i].startsWith('```')) { code.push(lines[i]); i++; }
    i++; // closing fence
    code.forEach(c => children.push(new Paragraph({
      spacing: { after: 0, line: 240 },
      shading: { type: ShadingType.CLEAR, color: 'auto', fill: 'F2F2F2' },
      indent: { left: 240 },
      children: [new TextRun({ text: c.length ? c : ' ', font: MONO, size: 18 })],
    })));
    children.push(new Paragraph({ spacing: { after: 120 }, children: [new TextRun({ text: '', size: 2 })] }));
    flushListState(); continue;
  }

  if (line.startsWith('|')) {
    const rows = [];
    while (i < lines.length && lines[i].trim().startsWith('|')) {
      const cells = lines[i].trim().replace(/^\|/, '').replace(/\|$/, '').split('|').map(c => c.trim());
      const isSep = cells.every(c => /^:?-{3,}:?$/.test(c));
      if (!isSep) rows.push(cells);
      i++;
    }
    if (rows.length) children.push(tableFrom(rows));
    children.push(new Paragraph({ spacing: { after: 120 }, children: [new TextRun({ text: '', size: 2 })] }));
    flushListState(); continue;
  }

  if (line.startsWith('> ') || line === '>') {
    const quoteParas = [];
    let buf = [];
    while (i < lines.length && (lines[i].startsWith('> ') || lines[i].trim() === '>')) {
      const q = lines[i].startsWith('> ') ? lines[i].slice(2) : '';
      if (q.trim() === '') { if (buf.length) { quoteParas.push(buf.join(' ')); buf = []; } }
      else buf.push(q.trim());
      i++;
    }
    if (buf.length) quoteParas.push(buf.join(' '));
    quoteParas.forEach(q => children.push(new Paragraph({
      indent: { left: 480 },
      spacing: { after: 100, line: 260 },
      border: { left: { style: BorderStyle.SINGLE, size: 18, color: 'AAAAAA', space: 8 } },
      children: inline(q, { size: 21, color: '333333' }),
    })));
    flushListState(); continue;
  }

  const bullet = line.match(/^(\s*)- (.*)$/);
  if (bullet) {
    const level = bullet[1].length >= 2 ? 1 : 0;
    children.push(new Paragraph({ numbering: { reference: 'bul', level, instance: 0 }, spacing: { after: 60 }, children: inline(bullet[2]) }));
    i++; flushListState(); continue;
  }

  const numbered = line.match(/^(\d+)\. (.*)$/);
  if (numbered) {
    if (!inNumList) { numInstance++; inNumList = true; }
    children.push(new Paragraph({ numbering: { reference: 'num', level: 0, instance: numInstance }, spacing: { after: 60 }, children: inline(numbered[2]) }));
    i++; continue;
  }

  if (line.trim() === '' ) { i++; flushListState(); continue; }
  if (line.trim() === '---') { i++; flushListState(); continue; }

  // plain paragraph
  children.push(new Paragraph({ alignment: AlignmentType.JUSTIFIED, spacing: { after: 140, line: 276 }, children: inline(line) }));
  i++; flushListState();
}

const doc = new Document({
  numbering: { config: [
    { reference: 'bul', levels: [
      { level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 540, hanging: 270 } } } },
      { level: 1, format: LevelFormat.BULLET, text: '◦', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 1000, hanging: 270 } } } },
    ]},
    { reference: 'num', levels: [
      { level: 0, format: LevelFormat.DECIMAL, text: '%1.', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 560, hanging: 360 } } } },
    ]},
  ]},
  styles: { default: {
    document: { run: { font: 'Times New Roman', size: 22 } },
    title:    { run: { font: 'Times New Roman', size: 32, bold: true, color: '000000' }, paragraph: { spacing: { after: 200 } } },
    heading1: { run: { font: 'Times New Roman', size: 27, bold: true, color: '000000' }, paragraph: { spacing: { before: 320, after: 160 } } },
    heading2: { run: { font: 'Times New Roman', size: 24, bold: true, color: '000000' }, paragraph: { spacing: { before: 260, after: 130 } } },
    heading3: { run: { font: 'Times New Roman', size: 22, bold: true, italics: true, color: '000000' }, paragraph: { spacing: { before: 220, after: 110 } } },
  }},
  sections: [{ properties: {}, children }],
});

Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync(OUT, buf);
  console.log('wrote', OUT, buf.length, 'bytes;', children.length, 'blocks');
});
