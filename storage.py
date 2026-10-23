print("=== Storage Converter ===")
storage_gb = float(input("Enter storage in GB: "))
storage_mb = storage_gb * 1024
print(storage_gb, "GB =", storage_mb, "MB")
storage_tb = storage_gb / 1024
print(storage_gb, "GB =", round(storage_tb, 4), "TB")
