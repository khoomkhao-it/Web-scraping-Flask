google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);

function drawChart() {
  var data = google.visualization.arrayToDataTable([
    ['Task', 'Hours per Day'],
    ['ผู้ป่วยสะสม', stack],
    ['ผู้ป่วยรายใหม่', newwer],
    ['ผู้ป่วยรุนแรง', heavy],
    ['เสียชีวิต', dead]
  ]);

  var options = {
    title: 'Covid-Daily'
  };

  var chart = new google.visualization.PieChart(document.getElementById('piechart'));

  chart.draw(data, options);
}
//////////////////////////////////////////////////////////////////////////////////////////////////////
google.charts.load('current', {packages: ['corechart', 'bar']});
google.charts.setOnLoadCallback(drawBasic);

function drawBasic() {

      var data = new google.visualization.DataTable();
      var data = google.visualization.arrayToDataTable([
        ['Name', 'Price'],
        ['ฟิวเซฟ แก๊สโซฮอล์91', Fgas91],            // RGB value
        ['ฟิวเซฟ ดีเซล', FDiesel],            // English color name
        ['อี20 แก๊สโซฮอล์', gasE20],
        ['ดีเซลB20	', DieselB20],
        ['ฟิวเซฟ ดีเซลB10', DieselB10],
        ['วี-เพาเวอร์ แก๊สโซฮอล์95', gas95],
        ['วี-เพาเวอร์ ดีเซล', VDiesel], // CSS-style declaration
      ]);

      var options = {
        title: 'ราคาน้ำมัน shell Thailand',
        hAxis: {
          title: 'ราคาน้ำมัน shell',
        },
        /*vAxis: {
          title: 'ราคา (scale of 1-35)'
        }*/
      };

      var chart = new google.visualization.ColumnChart(document.getElementById('columchart'));
      chart.draw(data, options);
    }