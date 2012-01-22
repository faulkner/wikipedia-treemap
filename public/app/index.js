// Change *namespace* to your namespace!
// This contains the module definition factory function, application state,
// events, and the router.
this.namespace = {
  // Assist with code organization, by breaking up logical components of code
  // into modules.
  module: function() {
    // Internal module cache.
    var modules = {};

    // Create a new module reference scaffold or load an existing module.
    return function(name) {
      // If this module has already been created, return it.
      if (modules[name]) {
        return modules[name];
      }

      // Create a module and save it under this name
      return modules[name] = { Views: {} };
    };
  }(),

  fetchTemplate: function(path, done) {
    window.JST = window.JST || {};

    // Should be an instant synchronous way of getting the template, if it
    // exists in the JST object.
    if (JST[path]) {
      return done(JST[path]);
    }

    // Fetch it asynchronously if not available from JST
    return $.get(path, function(contents) {
      var tmpl = _.template(contents);
      JST[path] = tmpl;

      done(tmpl);
    });
  },

  // Keep active application instances namespaced under an app object.
  app: _.extend({}, Backbone.Events)
};

// Treat the jQuery ready function as the entry point to the application.
// Inside this function, kick-off all initialization, everything up to this
// point should be definitions.
jQuery(function($) {

  var app = namespace.app;
  var App = namespace.module('chart');

  var Router = Backbone.Router.extend({
    routes: {
      '': 'index',
      ':hash': 'index',
      'chart/:hash/:source': 'chart'
    },

    index: function(hash) {
      var route = this;
      var chart = new App.Views.Chart();
      var nav = new App.Views.ChartNav();

      nav.render(function(el) {
        $('#nav').html(el);
      });
      chart.render(function(el) {
        $('#main').html(el);
        url = 'data/' + $('#type').val() + '?source=' + $('#source').val()
        load_chart(url);
      });
    },

    chart: function(type, source) {
      var route = this;
      var chart = new App.Views.Chart();
      var nav = new App.Views.ChartNav();

      nav.render(function(el) {
        $('#nav').html(el);
      });
      chart.render(function(el) {
        $('#main').html(el);
        $('#type').val(type);
        $('#source').val(source);
        url = 'data/' + $('#type').val() + '?source=' + $('#source').val()
        load_chart(url);
      });
    }

  });

  app.router = new Router();

  Backbone.history.start({ pushState: false });

  // All navigation that is relative should be passed through the navigate
  // method, to be processed by the router.  If the link has a data-bypass
  // attribute, bypass the delegation completely.
  $(document).on('click', 'a:not([data-bypass])', function(evt) {
    // Get the anchor href and protcol
    var href = $(this).attr('href');
    var protocol = this.protocol + '//';

    // Ensure the protocol is not part of URL, meaning its relative.
    if (href.slice(0, protocol.length) !== protocol) {
      evt.preventDefault();
      app.router.navigate(href, true);
    }
  });
});
