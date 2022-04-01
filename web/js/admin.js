// Graph
var ctx = document.getElementById("myChart");
setInterval(() => {
  fetch("http://raspberrypi:5000/weather").then((response) => response.json()).then((data) => {
    var myChart = new Chart(ctx, {
      type: "line",
      data: {
        labels: data.map(x => {
          const date = new Date(x.date)
    
          const hoursString = ('0' + date.getHours()).slice(-2);
          const minutesString = ('0' + date.getMinutes()).slice(-2);
          const secondsString = ('0' + date.getSeconds()).slice(-2);
          return `${hoursString}:${minutesString}:${secondsString}`
        }),
        datasets: [
          {
            data: data.map(x => x.temp),
            lineTension: 0,
            backgroundColor: "transparent",
            borderColor: "#00b74a",
            borderWidth: 4,
            pointBackgroundColor: "#00b74a",
          },
          {
            data: data.map(x => x.hum),
            lineTension: 0,
            backgroundColor: "transparent",
            borderColor: "#f93154",
            borderWidth: 4,
            pointBackgroundColor: "#f93154",
          },
        ],
      },
      options: {
        scales: {
          yAxes: [
            {
              ticks: {
                beginAtZero: false,
              },
            },
          ],
        },
        legend: {
          display: false,
        },
      },
    });
  })
  
}, 5000)
