document.addEventListener('DOMContentLoaded', () => {
    const splash = document.getElementById('splash-screen');
    const video = document.getElementById('splash-video');
    const enterBtn = document.getElementById('enter-btn');
    const hiddenElements = document.querySelectorAll('.hidden-initially');

    // Show video once it's ready
    video.addEventListener('canplaythrough', () => {
        video.style.opacity = '1';
    });

    enterBtn.addEventListener('click', () => {
        // Start playing video with sound
        video.play();
        enterBtn.style.opacity = '0';
        enterBtn.style.pointerEvents = 'none';

        // When video ends, dissolve splash screen
        video.onended = () => {
            splash.classList.add('dissolve');
            
            // Show main content after a small delay
            setTimeout(() => {
                hiddenElements.forEach(el => el.classList.add('fade-in'));
            }, 500);
        };
    });
});
