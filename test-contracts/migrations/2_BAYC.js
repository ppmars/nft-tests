var Address = artifacts.require("Address");
var BoredApeYachtClub = artifacts.require("BoredApeYachtClub")

module.exports = function (deployer) {
  deployer.deploy(Address);
    deployer.deploy(BoredApeYachtClub, "BoredAYC", "BAYC", 10000, 0);
};

