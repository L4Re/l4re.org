-- vim:ft=lua
local L4 = require("L4");
local ld = L4.default_loader;

local hw_desc_file = "";
if L4.Info.arch() == "arm64" then
  hw_desc_file = "rom/hw_devices.io";
end

local vbus_eth  = ld:new_channel();
ld:start({ caps = {
                    sigma0   = L4.Env.sigma0;
                    icu      = L4.Env.icu;
                    iommu    = L4.Env.iommu;
                    ethdevs  = vbus_eth:svr();
                  },
         },
         "rom/io -vvvv " .. hw_desc_file .. " rom/ixl.vbus");

local vswitch = ld:new_channel();
ld:start({ caps = { vbus = vbus_eth, svr = vswitch:svr(); }, },
         "rom/l4vio_switch");

ld:start({}, "rom/curl --version");

ld:start({ caps = { virtnet = vswitch:create(0), etc = L4.Env.rom  }, },
         "rom/curl -s http://ftp.de.debian.org/debian/",
         { IFCONFIG_IP4_vn0="dhcp" });
