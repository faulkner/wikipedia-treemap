(function() {
  var div, h, treemap, w;

  w = 960;

  h = 500;

  this.color = d3.scale.category20c();

  treemap = d3.layout.treemap().size([w, h]).sticky(true).value(function(d) {
    return d.size;
  });

  div = d3.select("#chart").append("div").style("position", "relative").style("width", w + "px").style("height", h + "px");

  $(".buttons").hide();

  this.load_chart = function(url) {
    return d3.json(url, function(json) {
      $(".buttons").show();
      div.data([json]).selectAll("div").data(treemap.nodes).enter().append("div").attr("class", "cell").style("background", function(d) {
        if (d.children) {
          return window.color(d.name);
        } else {
          return null;
        }
      }).call(cell).text(function(d) {
        if (d.children) {
          return null;
        } else {
          return d.name;
        }
      });
      d3.select("#size").on("click", function() {
        div.selectAll("div").data(treemap.value(function(d) {
          return d.size;
        })).transition().duration(1500).call(cell);
        d3.select("#size").classed("active", true);
        return d3.select("#count").classed("active", false);
      });
      return d3.select("#count").on("click", function() {
        div.selectAll("div").data(treemap.value(function(d) {
          return 1;
        })).transition().duration(1500).call(cell);
        d3.select("#size").classed("active", false);
        return d3.select("#count").classed("active", true);
      });
    });
  };

  this.cell = function() {
    return this.style("left", function(d) {
      return d.x + "px";
    }).style("top", function(d) {
      return d.y + "px";
    }).style("width", function(d) {
      return d.dx - 1 + "px";
    }).style("height", function(d) {
      return d.dy - 1 + "px";
    });
  };

}).call(this);
