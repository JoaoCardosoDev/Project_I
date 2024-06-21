window.onload = () => {
    console.log("gello")
    const overlay = document.querySelector('.overlay')
    const crtFolder = document.querySelector('.createFolder')
    const crtFile = document.querySelector('.fileCreatecard')

    const newFolder = document.querySelector('#newFolderbttn')
    newFolder.addEventListener("click", function(e) {
        overlay.style.display = "flex";
        crtFolder.style.display = "flex"
    })
    
    const upFile = document.querySelector('#upFilebttn')
    upFile.addEventListener("click", function(e) {
        overlay.style.display = "flex";
        crtFile.style.display = "flex"
    })



    console.log(newFolder)
    overlay.addEventListener("click", function (e) {
        if (e.target !== this)
            return;
        overlay.style.display = "none";
        crtFile.style.display = "none"
        crtFolder.style.display = "none"
      });
}