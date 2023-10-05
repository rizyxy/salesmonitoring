const ctx = document.getElementById('myChart');

new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        datasets: [{
            label: '# of Votes',
            data: [12, 19, 3, 5, 30, 3],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

function changeContent(page) {
    document.getElementById('page-title').textContent = page;
}

function activateYear() {
    document.getElementById('year').classList.add('active')
    document.getElementById('month').classList.remove('active')
    document.getElementById('week').classList.remove('active')
}

function activateMonth() {
    document.getElementById('year').classList.remove('active')
    document.getElementById('month').classList.add('active')
    document.getElementById('week').classList.remove('active')
}

function activateWeek() {
    document.getElementById('year').classList.remove('active')
    document.getElementById('month').classList.remove('active')
    document.getElementById('week').classList.add('active')
}