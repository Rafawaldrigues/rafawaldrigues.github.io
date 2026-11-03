const headerLinks = [...document.querySelectorAll('.site-nav a')];
const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
const finePointer = window.matchMedia('(hover: hover) and (pointer: fine)');
const sections = headerLinks
  .map((link) => document.querySelector(link.getAttribute('href')))
  .filter(Boolean);

if ('IntersectionObserver' in window) {
  const observer = new IntersectionObserver((entries) => {
    const visible = entries
      .filter((entry) => entry.isIntersecting)
      .sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0];

    if (!visible) return;
    headerLinks.forEach((link) => {
      const active = link.getAttribute('href') === `#${visible.target.id}`;
      link.toggleAttribute('aria-current', active);
    });
  }, { rootMargin: '-35% 0px -55%', threshold: [0, 0.25, 0.5] });

  sections.forEach((section) => observer.observe(section));

  const evidenceObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      entry.target.classList.add('is-evidence-live');
      evidenceObserver.unobserve(entry.target);
    });
  }, { rootMargin: '0px 0px -18%', threshold: 0.25 });

  document.querySelectorAll('.feature-project, .project-study')
    .forEach((item) => evidenceObserver.observe(item));
}

document.documentElement.classList.add('motion-ready');
requestAnimationFrame(() => document.body.classList.add('is-ready'));

const hero = document.querySelector('.hero-frame');

if (hero && finePointer.matches && !reducedMotion.matches) {
  let pointerFrame;

  const renderPointer = (event) => {
    const bounds = hero.getBoundingClientRect();
    const x = Math.min(1, Math.max(0, (event.clientX - bounds.left) / bounds.width));
    const y = Math.min(1, Math.max(0, (event.clientY - bounds.top) / bounds.height));
    const dx = x - 0.5;
    const dy = y - 0.5;

    hero.style.setProperty('--light-x', `${(x * 100).toFixed(2)}%`);
    hero.style.setProperty('--light-y', `${(y * 100).toFixed(2)}%`);
    hero.style.setProperty('--left-x', `${(dx * -10).toFixed(2)}px`);
    hero.style.setProperty('--left-y', `${(dy * -7).toFixed(2)}px`);
    hero.style.setProperty('--right-x', `${(dx * 10).toFixed(2)}px`);
    hero.style.setProperty('--right-y', `${(dy * 7).toFixed(2)}px`);
    hero.style.setProperty('--glass-x', `${(dx * 4).toFixed(2)}px`);
    hero.style.setProperty('--glass-y', `${(dy * 3).toFixed(2)}px`);
  };

  hero.addEventListener('pointermove', (event) => {
    cancelAnimationFrame(pointerFrame);
    pointerFrame = requestAnimationFrame(() => renderPointer(event));
  });

  hero.addEventListener('pointerleave', () => {
    cancelAnimationFrame(pointerFrame);
    ['--left-x', '--left-y', '--right-x', '--right-y', '--glass-x', '--glass-y']
      .forEach((property) => hero.style.setProperty(property, '0px'));
    hero.style.setProperty('--light-x', '50%');
    hero.style.setProperty('--light-y', '34%');
  });
}
