w = 960
h = 500
@color = d3.scale.category20c()

treemap = d3.layout.treemap()
    .size([w, h])
    .sticky(true)
    .value((d) -> d.size)

div = d3.select('#chart').append('div')
    .style('position', 'relative')
    .style('width', w + 'px')
    .style('height', h + 'px')

# TODO: something less hacky menu hiding
# TODO: spinner for slow-loading charts
$('.buttons').hide()

@load_chart = (url) ->
    d3.json url, (json) ->
      $('.buttons').show()
      div.data([json]).selectAll('div')
          .data(treemap.nodes)
        .enter().append('div')
          .attr('class', 'cell')
          .style('background', (d) -> if d.children then window.color(d.name) else null)
          .call(cell)
          .text((d) -> d.name + ' (' + Math.round(100 * d.size / json.value) + '% : ' + d.size + ')' if not d.children)

      d3.select('#size').on 'click', () ->
        div.selectAll('div')
            .data(treemap.value (d) -> d.size)
          .transition()
            .duration(1500)
            .call(cell)

        d3.select('#size').classed 'active', true
        d3.select('#count').classed 'active', false

      d3.select('#count').on 'click', () ->
        div.selectAll('div')
            .data(treemap.value (d) -> 1)
          .transition()
            .duration(1500)
            .call(cell)

        d3.select('#size').classed 'active', false
        d3.select('#count').classed 'active', true

@cell = () ->
  @.style('left', (d) -> d.x + 'px')
   .style('top', (d) -> d.y + 'px')
   .style('width', (d) -> d.dx - 1 + 'px')
   .style('height', (d) -> d.dy - 1 + 'px')
