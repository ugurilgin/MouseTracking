let pageCoords = [];
let isNewDataCaptured = false;

setInterval(() => {
    if (isNewDataCaptured) {

        const XHR = new XMLHttpRequest();

        XHR.addEventListener('load', () => {
            isNewDataCaptured = false;
            pageCoords = []
        });
        XHR.open('POST', 'http://localhost:5000')
        XHR.setRequestHeader("Content-Type", "application/json;charset=UTF-8")
        XHR.send(JSON.stringify(pageCoords))
    }
}, 1000)

document.onmousemove = (e) => {
    isNewDataCaptured = true;
    pageCoords.push({
        x: e.pageX,
        y: e.pageY,
        click: '0'
    })
};
