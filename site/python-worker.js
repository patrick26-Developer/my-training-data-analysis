import { loadPyodide } from "https://cdn.jsdelivr.net/pyodide/v314.0.8/full/pyodide.mjs";

const runtime = loadPyodide();

self.onmessage = async ({ data }) => {
  let pyodide;
  try {
    pyodide = await runtime;
    const responses = data.inputs ? data.inputs.split("\n") : [];
    let line = 0;
    let written = 0;
    const write = (text) => {
      if (written >= 30_000) return;
      const chunk = text.slice(0, 30_000 - written);
      written += chunk.length + 1;
      self.postMessage({ kind: "output", text: chunk });
    };
    pyodide.setStdout({ batched: write });
    pyodide.setStderr({ batched: write });
    pyodide.setStdin({ stdin: () => responses[line++] ?? null });
    self.postMessage({ kind: "running" });
    const createDict = pyodide.globals.get("dict");
    const globals = createDict([["__name__", "__main__"]]);
    createDict.destroy();
    try {
      const result = await pyodide.runPythonAsync(data.code, { globals });
      if (result && typeof result.destroy === "function") result.destroy();
    } finally {
      globals.destroy();
    }
    self.postMessage({ kind: "done" });
  } catch (error) {
    self.postMessage({ kind: "error", text: String(error), reset: !pyodide });
  }
};
