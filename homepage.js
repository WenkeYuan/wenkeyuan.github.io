const buttons = document.querySelectorAll('[data-filter]');
const papers = [...document.querySelectorAll('.paper')];
function filterPapers(category) {
  let count = 0;
  for (const paper of papers) {
    paper.hidden = category !== 'all' && paper.dataset.category !== category;
    if (!paper.hidden) count++;
  }
  for (const button of buttons) {
    const active = button.dataset.filter === category;
    button.classList.toggle('active', active);
    button.setAttribute('aria-pressed', String(active));
  }
  document.querySelector('#paper-count').textContent = `${count} publications`;
}
buttons.forEach(button => button.addEventListener('click', () => filterPapers(button.dataset.filter)));
filterPapers('all');
document.querySelector('#year').textContent = new Date().getFullYear();
