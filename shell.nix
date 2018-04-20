with import <nixpkgs> {};
(pkgs.python3.withPackages(ps: with ps; [numpy matplotlib pandas jupyter basemap])).env
