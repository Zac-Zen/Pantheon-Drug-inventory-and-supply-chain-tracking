USE `root-database`;
SELECT drugs.id, drugs.drug_name, drugs.expiry_date, drugs.present_quantity, drugs.original_quantity, drugs.cost, drug_mini.present_quantity
FROM `root-database`.drugs drugs
JOIN `stock-track-database`.drug_mini drug_mini
ON drugs.id = drug_mini.drug_id
   AND drugs.drug_name = drug_mini.drug_name
   AND drugs.expiry_date = drug_mini.expiry_date;
