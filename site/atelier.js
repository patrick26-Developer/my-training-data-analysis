const dialog = document.querySelector("dialog");
const code = document.querySelector("#code");
const inputs = document.querySelector("#inputs");
const run = document.querySelector("#run");
const stop = document.querySelector("#stop");
const status = document.querySelector("#status");
const output = document.querySelector("#output");
let worker;
let timer;

const mobile = matchMedia("(max-width: 49rem)");
const compactOutline = matchMedia("(max-width: 68rem)");
const courseMenu = document.querySelector(".course-menu");
const outlineMenu = document.querySelector(".outline details");

function updateMenus() {
  courseMenu.open = !mobile.matches;
  if (outlineMenu) outlineMenu.open = !compactOutline.matches;
}

updateMenus();
mobile.addEventListener("change", updateMenus);
compactOutline.addEventListener("change", updateMenus);

document.querySelector("[data-open]").addEventListener("click", () => dialog.showModal());
document.querySelectorAll(".example button").forEach((button) => {
  button.addEventListener("click", () => {
    code.value = button.closest(".example").querySelector("code").textContent;
    output.textContent = "";
    status.textContent = "";
    dialog.showModal();
  });
});

function finish(message, resetWorker = false) {
  clearTimeout(timer);
  if (resetWorker) {
    worker?.terminate();
    worker = undefined;
  }
  status.textContent = message;
  run.disabled = false;
  stop.disabled = true;
}

function append(line) {
  if (output.textContent.length < 30_000) {
    output.textContent += line.slice(0, 30_000) + "\n";
  }
}

run.addEventListener("click", () => {
  run.disabled = true;
  stop.disabled = false;
  output.textContent = "";
  status.textContent = worker ? "Exécution…" : "Chargement de Python…";
  try {
    worker ??= new Worker("/python-worker.js", { type: "module" });
    worker.onmessage = ({ data }) => {
      if (data.kind === "running") {
        status.textContent = "Exécution…";
        clearTimeout(timer);
        timer = setTimeout(() => finish("Temps d’exécution dépassé.", true), 15_000);
      }
      if (data.kind === "output") append(data.text);
      if (data.kind === "done") finish("Exécution terminée.");
      if (data.kind === "error") {
        append(data.text);
        finish("Exécution interrompue.", data.reset);
      }
    };
    worker.onerror = () => finish("Impossible de charger Python. Vérifie ta connexion.", true);
    timer = setTimeout(() => finish("Le chargement a pris trop de temps.", true), 60_000);
    worker.postMessage({ code: code.value, inputs: inputs.value });
  } catch {
    finish("L’atelier Python est indisponible dans ce navigateur.", true);
  }
});
stop.addEventListener("click", () => finish("Exécution arrêtée.", true));
dialog.addEventListener("close", () => {
  if (run.disabled) finish("Exécution arrêtée.", true);
});
