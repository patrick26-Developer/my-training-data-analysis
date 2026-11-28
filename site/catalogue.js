const filters = document.querySelector(".course-filters");
const results = document.querySelector(".filter-result");
const normalize = (text) => text.normalize("NFD").replace(/\p{Diacritic}/gu, "").toLowerCase();
const courses = Array.from(document.querySelectorAll(".course-card"), (card) => ({
  card,
  text: normalize(card.textContent),
}));

function filterCourses() {
  const fields = new FormData(filters);
  const query = normalize(fields.get("query").trim());
  const status = fields.get("status");
  let visible = 0;
  for (const { card, text } of courses) {
    card.hidden = !(text.includes(query) && (!status || card.dataset.status === status));
    if (!card.hidden) visible++;
  }
  results.textContent = visible === 0 ? "Aucun parcours correspondant." : `${visible} parcours affichés`;
}

filters.addEventListener("submit", (event) => event.preventDefault());
filters.addEventListener("input", filterCourses);
filterCourses();
results.hidden = false;
filters.hidden = false;
