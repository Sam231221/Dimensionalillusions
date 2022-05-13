document.addEventListener('DOMContentLoaded', () => {
  hljs.highlightAll();

  const getcode= document.getElementById('code');
  const copyButton = document.getElementById('copy-button');
  const copySuccess = document.getElementById('copy-success');

  const copyTextHandler = () => {
    const text = getcode.innerText;
    navigator.clipboard.writeText(text).then(
      () => {
        copySuccess.classList.add('show-message');
        setTimeout(() => {
          copySuccess.classList.remove('show-message');
        }, 2500);
      },
      () => {
        console.log('Error writing to the clipboard');
      }
    );
  };
  copyButton.addEventListener('click', copyTextHandler);
});

document.addEventListener('DOMContentLoaded', (event) => {
  document.querySelectorAll('pre code').forEach((el) => {
    hljs.highlightElement(el);
  });
});