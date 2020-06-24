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
        for (let n of navLinks) {
            n.classList.remove("active")
        }
        e.target.classList.add("active")
        fetch(e.target.href)
            .then(res => res.json())
            .then(json => Plotly.react(graphDiv, json, layout))
        e.preventDefault()
    }
}

var trae1 = {
    x: [1, 2, 3, 4],
    y: [10, 15, 13, 17],
    type: 'scatter',
    name: 'things'
};

var trace2 = {
    x: [1, 2, 3, 4],
    y: [16, 5, 11, 9],
    type: 'scatter'
};

var data = [trae1, trace2];


var config = {responsive: true}

Plotly.newPlot(graphDiv, data, layout, config);