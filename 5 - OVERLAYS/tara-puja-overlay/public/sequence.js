// Loads content.json and flattens the sequence into a flat list of "steps"
// the controller walks through. The Taras loop is represented once in the
// data; here we just mark where it starts and ends so the controller can
// decide whether "next" advances past it or loops back for another pass.

async function loadSequence() {
  const res = await fetch("content.json");
  const content = await res.json();
  const raw = content.sequence;

  const steps = [];
  let loopStart = null, loopEnd = null;

  for (const item of raw) {
    if (item.type === "loop_start") { loopStart = steps.length; continue; }
    if (item.type === "loop_end") { loopEnd = steps.length - 1; continue; }
    steps.push(item);
  }

  return { content, steps, loopStart, loopEnd };
}
