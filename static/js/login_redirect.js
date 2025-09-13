document.addEventListener('DOMContentLoaded', function() {
  const dropdownLinks = document.querySelectorAll('.dropdown-content a');
  dropdownLinks.forEach(link => {
    link.addEventListener('click', function(e) {
      e.preventDefault();
      if (link.textContent.includes('Admin')) {
        window.location.href = '/accounts/login/?type=admin';
      } else if (link.textContent.includes('Doctor')) {
        window.location.href = '/accounts/login/?type=doctor';
      } else if (link.textContent.includes('Patient')) {
        window.location.href = '/accounts/login/?type=patient';
      }
    });
  });
});

document.addEventListener('DOMContentLoaded', function () {
  const toggleBtn = document.getElementById('theme-toggle');
  const body = document.body;

  if (!toggleBtn) {
    console.warn("No theme-toggle button found.");
    return;
  }

  // Load saved theme
  const savedTheme = localStorage.getItem('theme');
  if (savedTheme === 'dark') {
    body.classList.add('dark-mode');
  }

  // Toggle theme on click
  toggleBtn.addEventListener('click', function () {
    body.classList.toggle('dark-mode');
    const isDark = body.classList.contains('dark-mode');
    localStorage.setItem('theme', isDark ? 'dark' : 'light');
  });
});
