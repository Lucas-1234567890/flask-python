document.addEventListener('DOMContentLoaded', () => {
  const inputFoto = document.querySelector('input[type="file"][name="foto_perfil"]');
  const previewImg = document.querySelector('.image img');

  if(inputFoto && previewImg){
    inputFoto.addEventListener('change', (event) => {
      const file = event.target.files[0];
      if(file){
        const reader = new FileReader();
        reader.onload = (e) => {
          previewImg.src = e.target.result;
        }
        reader.readAsDataURL(file);
      }
    });
  }

  const form = document.querySelector('form');
  if(form){
    form.addEventListener('submit', (e) => {
      const email = form.querySelector('input[name="email"]');
      if(email && !email.value.includes('@')){
        e.preventDefault();
        alert('Email inválido!');
        email.focus();
        return;
      }
      const btn = form.querySelector('button[type="submit"]');
      if(btn){
        btn.disabled = true;
        btn.innerText = 'Enviando...';
        btn.classList.add('loading');
      }
    });
  }
});
