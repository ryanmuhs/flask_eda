var myPlot = echarts.init(document.getElementById('plot'));
option = {
    {% for kol in kolom %}
    xAxis: {
        data: {{ kol }}
    },
    yAxis: {},
    {% endfor %}
    series: [

        {
            type: 'bar',
            data: [23, 24, 18, 25, 27, 28, 25]
        }
    ]
};

option && myPlot.setOption(option)

var myLine = echarts.init(document.getElementById('line'));
option = {
    xAxis: {
      data: ['A', 'B', 'C', 'D', 'E']
    },
    yAxis: {},
    series: [
      {
        data: [10, 22, 28, 43, 49],
        type: 'line',
        stack: 'x'
      },
      {
        data: [5, 4, 3, 5, 10],
        type: 'line',
        stack: 'x'
      }
    ]
  };
option && myLine.setOption(option)
