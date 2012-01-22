(function(Chart) {

  Chart.Model = Backbone.Model.extend({ /* ... */ });
  Chart.Collection = Backbone.Collection.extend({ /* ... */ });
  Chart.Router = Backbone.Router.extend({ /* ... */ });

  Chart.Views.ChartNav = Backbone.View.extend({
    template: 'app/t/chartnav.html',

    events: {
      'change #source': 'reloadChart',
      'change #type': 'reloadChart'
    },

    reloadChart: function() {
        type = $('#type').val()
        url = 'data/' + type + '?source=' + $('#source').val()
        Backbone.history.navigate('chart/' + type + '/' + $('#source').val(), true)
        //window.location.href = '#' + this.hash + '?source=' + $('#source').val()
        //load_chart(url);
    },
    render: function(done) {
      var view = this;

      namespace.fetchTemplate(this.template, function(tmpl) {
        view.el.innerHTML = tmpl();

        done(view.el);
      });
    }
  });

  Chart.Views.Chart = Backbone.View.extend({
    template: 'app/t/chart.html',

    render: function(done) {
      var view = this;

      // Fetch the template, render it to the View element and call done.
      namespace.fetchTemplate(this.template, function(tmpl) {
        view.el.innerHTML = tmpl();

        done(view.el);
      });
    }
  });

})(namespace.module('chart'));
