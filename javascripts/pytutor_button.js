window.onload = function() {
  document.querySelectorAll("div.pytutor_button.highlight").forEach(function(block) {
    const codeElement = block.querySelector("code");
    if (codeElement) {
      const code = codeElement.textContent.trim();
      const encodedCode = encodeURIComponent(code);
      const buttonUrl = `https://pythontutor.com/render.html#code=${encodedCode}&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false`;

      const button = document.createElement("a");
      button.href = buttonUrl;
      button.target = "_blank";  // Neuer Tab
      button.rel = "noopener noreferrer";  // Sicherheitsmaßnahme
      button.className = "md-button";
      button.innerHTML = '<i class="fa-solid fa-bug"></i> Code im Debugger ansehen';
      block.insertAdjacentElement('afterend', button);
    }
  });
};
