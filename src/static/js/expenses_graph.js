let graphDiv = document.getElementById("expensesGraph")
let nav = document.getElementById("graph-nav")
let navLinks = nav.getElementsByClassName('nav-link')
let layout = {
    font: {size: 14},
    xaxis: {
        type: 'date'
    },
    yaxis: {
        ticksuffix: '€'
    }
};

for (let navLink of navLinks) {
    navLink.onclick = e => {
        graphDiv.style.opacity = "0.5"
        for (let n of navLinks) {
            n.classList.remove("active")
        }
        e.target.classList.add("active")
        fetch(e.target.href)
            .then(res => res.json())
            .then(json => Plotly.react(graphDiv, json, layout))
            .then(() => graphDiv.style.opacity = "1")
        e.preventDefault()
    }
}

let config = {responsive: true}
Plotly.newPlot(graphDiv, [], layout, config);
navLinks[0].click()