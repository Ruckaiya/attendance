if(window.innerWidth <= 745){
    document.getElementById('dashboard-slidebar').classList.add('dashboard-slidebar-hidden')
}

Array.from(document.getElementsByClassName('dashboard-parent-dropdown')).forEach(element =>{
    element.click()
})

function showOptions() {
    
    let dropDownElm = event.currentTarget
    let dropDownIcon = dropDownElm.querySelector('.dashboard-dropdown-icon')
    if(dropDownElm.parentElement.style.height == '50px'){
        dropDownElm.parentElement.style.height = 'auto'

        dropDownIcon.style.transform = 'rotateZ(270deg)'
        let dropDownItems = Array.from(dropDownElm.parentElement.children)

        for (let i = 0; i < dropDownItems.length; i++) {
            if(i==0){
                continue
            }
            const element = dropDownItems[i];
            element.style.opacity = '1'
            element.style.transform = 'scale(1)'
            
        }


    }
    else{
        dropDownIcon.style.transform = 'rotateZ(360deg)'

        dropDownElm.parentElement.style.height = '50px'

        let dropDownItems = Array.from(dropDownElm.parentElement.children)

        for (let i = 0; i < dropDownItems.length; i++) {
            if(i==0){
                continue
            }
            const element = dropDownItems[i];
            element.style.opacity = '0'
            element.style.transform = 'scale(0)'


            
        }
    }
    
}


let messageDropDownIcon = document.getElementById('dashboard-message-icon')
let messageDropDownIconDiv = document.getElementById('dashboard-message-icon-dropdown')
let notificationDropDownIcon = document.getElementById('dashboard-notification-icon')
let notificationDropDownIconDiv = document.getElementById('dashboard-notification-icon-dropdown')
let otherArr = Array.from(document.getElementsByClassName('dashboard-message-dropdown-cont'))
messageDropDownIcon.addEventListener('click', ()=>{
    if(messageDropDownIconDiv.classList.contains('dashboard-show-dropdown')){
        messageDropDownIconDiv.classList.remove('dashboard-show-dropdown')
        messageDropDownIconDiv.classList.add('dashboard-hide-dropdown')
    }
    else{
        
        messageDropDownIconDiv.classList.add('dashboard-show-dropdown')
        messageDropDownIconDiv.classList.remove('dashboard-hide-dropdown')

    }
    notificationDropDownIconDiv.classList.remove('dashboard-show-dropdown')
    notificationDropDownIconDiv.classList.add('dashboard-hide-dropdown')
        

})

notificationDropDownIcon.addEventListener('click', ()=>{
    if(notificationDropDownIconDiv.classList.contains('dashboard-show-dropdown')){
        notificationDropDownIconDiv.classList.remove('dashboard-show-dropdown')
        notificationDropDownIconDiv.classList.add('dashboard-hide-dropdown')
    }
    else{
        notificationDropDownIconDiv.classList.add('dashboard-show-dropdown')
        notificationDropDownIconDiv.classList.remove('dashboard-hide-dropdown')
    }
    messageDropDownIconDiv.classList.remove('dashboard-show-dropdown')
    messageDropDownIconDiv.classList.add('dashboard-hide-dropdown')
        
})



/* Get the documentElement (<html>) to display the page in fullscreen */
var elem = document.documentElement;
let goFullScreenIcon = document.getElementById('dashboard-go-full-screen-icon')
let fullScreen = false
goFullScreenIcon.addEventListener('click', ()=>{
    if(!fullScreen){
        openFullscreen()
        goFullScreenIcon.innerHTML = `<i class="fas fa-compress-arrows-alt"></i>`
    }
    else{
        closeFullscreen()
        goFullScreenIcon.innerHTML = `<i class="fas fa-expand-arrows-alt"></i>`

    }
})
/* View in fullscreen */
function openFullscreen() {
  if (elem.requestFullscreen) {
    elem.requestFullscreen();
    fullScreen = true
} else if (elem.webkitRequestFullscreen) { /* Safari */
    elem.webkitRequestFullscreen();
    fullScreen = true
} else if (elem.msRequestFullscreen) { /* IE11 */
    elem.msRequestFullscreen();
    fullScreen = true
  }
}

/* Close fullscreen */
function closeFullscreen() {
  if (document.exitFullscreen) {
    document.exitFullscreen();
    fullScreen = false
    
} else if (document.webkitExitFullscreen) { /* Safari */
    document.webkitExitFullscreen();
    fullScreen = false
} else if (document.msExitFullscreen) { /* IE11 */
    document.msExitFullscreen();
    fullScreen = false
  }
}



let slideBar = document.getElementById('dashboard-slidebar')
let slideBarIcon = document.getElementById('dashboard-slidebar-icon')

slideBarIcon.addEventListener('click', ()=>{
    slideBar.classList.toggle('dashboard-slidebar-hidden')
    document.getElementById('dashboard-content-wraper').classList.toggle('dashboard-content-wraper-full-width')
})