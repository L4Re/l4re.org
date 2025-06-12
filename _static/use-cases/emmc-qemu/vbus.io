Io.add_vbus("sdhci", Io.Vi.System_bus
{
  pci_08 = wrap(Io.system_bus():match("PCI/CC_0805")), -- SDHCI
})
