'use strict';

var React = require("react");
var LogoJs = require("./logo.js");

var make = LogoJs.Android;

var Android = {
  make: make
};

var make$1 = LogoJs.Angular;

var Angular = {
  make: make$1
};

var make$2 = LogoJs.Apple;

var Apple = {
  make: make$2
};

var make$3 = LogoJs.Aws;

var Aws = {
  make: make$3
};

var make$4 = LogoJs.C;

var C = {
  make: make$4
};

var make$5 = LogoJs.Cpp;

var Cpp = {
  make: make$5
};

var make$6 = LogoJs.Django;

var Django = {
  make: make$6
};

var make$7 = LogoJs.Docker;

var Docker = {
  make: make$7
};

var make$8 = LogoJs.ElasticSearch;

var ElasticSearch = {
  make: make$8
};

var make$9 = LogoJs.Electron;

var Electron = {
  make: make$9
};

var make$10 = LogoJs.Git;

var Git = {
  make: make$10
};

var make$11 = LogoJs.Go;

var Go = {
  make: make$11
};

var make$12 = LogoJs.GoogleCloud;

var GoogleCloud = {
  make: make$12
};

var make$13 = LogoJs.Grpc;

var Grpc = {
  make: make$13
};

var make$14 = LogoJs.Heroku;

var Heroku = {
  make: make$14
};

var make$15 = LogoJs.Java;

var Java = {
  make: make$15
};

var make$16 = LogoJs.Javascript;

var Javascript = {
  make: make$16
};

var make$17 = LogoJs.Melvin;

var Melvin = {
  make: make$17
};

var make$18 = LogoJs.Mongodb;

var Mongodb = {
  make: make$18
};

var make$19 = LogoJs.Mysql;

var Mysql = {
  make: make$19
};

var make$20 = LogoJs.Nodejs;

var Nodejs = {
  make: make$20
};

var make$21 = LogoJs.Postgres;

var Postgres = {
  make: make$21
};

var make$22 = LogoJs.Python;

var Python = {
  make: make$22
};

var make$23 = LogoJs.React;

var Reactjs = {
  make: make$23
};

var make$24 = LogoJs.Reasonml;

var Reasonml = {
  make: make$24
};

var make$25 = LogoJs.Redis;

var Redis = {
  make: make$25
};

var make$26 = LogoJs.Swift;

var Swift = {
  make: make$26
};

var make$27 = LogoJs.Typescript;

var Typescript = {
  make: make$27
};

var make$28 = LogoJs.Unknown;

var Unknown = {
  make: make$28
};

function Logo(Props) {
  var name = Props.name;
  switch (name) {
    case "android" :
        return React.createElement(make, { });
    case "angular" :
        return React.createElement(make$1, { });
    case "apple" :
        return React.createElement(make$2, { });
    case "aws" :
        return React.createElement(make$3, { });
    case "c" :
        return React.createElement(make$4, { });
    case "cpp" :
        return React.createElement(make$5, { });
    case "django" :
        return React.createElement(make$6, { });
    case "docker" :
        return React.createElement(make$7, { });
    case "elasticSearch" :
        return React.createElement(make$8, { });
    case "electron" :
        return React.createElement(make$9, { });
    case "git" :
        return React.createElement(make$10, { });
    case "go" :
        return React.createElement(make$11, { });
    case "googleCloud" :
        return React.createElement(make$12, { });
    case "grpc" :
        return React.createElement(make$13, { });
    case "heroku" :
        return React.createElement(make$14, { });
    case "java" :
        return React.createElement(make$15, { });
    case "javascript" :
        return React.createElement(make$16, { });
    case "mongodb" :
        return React.createElement(make$18, { });
    case "mysql" :
        return React.createElement(make$19, { });
    case "nodejs" :
        return React.createElement(make$20, { });
    case "postgres" :
        return React.createElement(make$21, { });
    case "python" :
        return React.createElement(make$22, { });
    case "reactjs" :
        return React.createElement(make$23, { });
    case "reasonml" :
        return React.createElement(make$24, { });
    case "redis" :
        return React.createElement(make$25, { });
    case "swift" :
        return React.createElement(make$26, { });
    case "typescript" :
        return React.createElement(make$27, { });
    default:
      return React.createElement(make$28, { });
  }
}

var make$29 = Logo;

exports.Android = Android;
exports.Angular = Angular;
exports.Apple = Apple;
exports.Aws = Aws;
exports.C = C;
exports.Cpp = Cpp;
exports.Django = Django;
exports.Docker = Docker;
exports.ElasticSearch = ElasticSearch;
exports.Electron = Electron;
exports.Git = Git;
exports.Go = Go;
exports.GoogleCloud = GoogleCloud;
exports.Grpc = Grpc;
exports.Heroku = Heroku;
exports.Java = Java;
exports.Javascript = Javascript;
exports.Melvin = Melvin;
exports.Mongodb = Mongodb;
exports.Mysql = Mysql;
exports.Nodejs = Nodejs;
exports.Postgres = Postgres;
exports.Python = Python;
exports.Reactjs = Reactjs;
exports.Reasonml = Reasonml;
exports.Redis = Redis;
exports.Swift = Swift;
exports.Typescript = Typescript;
exports.Unknown = Unknown;
exports.make = make$29;
/* make Not a pure module */
