# These and other macros are documented in
# ../droid-configs-device/droid-configs.inc
%define device flo
%define vendor asus
%define vendor_pretty Asus
%define device_pretty Nexus 7 (2013 WiFi)

# Adjust this for your device
%define pixel_ratio 1.0

# Community HW adaptations need this
%define community_adaptation 1

Provides: ofono-configs
Obsoletes: ofono-configs-mer

%include droid-configs-device/droid-configs.inc
