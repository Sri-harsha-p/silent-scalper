# Silent Scalper

Silent Scalper is a cloud-based dental image validation and processing system. It scans uploaded dental images and their associated metadata, validates the data, stores valid entries in AWS DynamoDB, and handles invalid or corrupted files by moving them to a quarantine S3 bucket. It also sends email alerts via AWS SNS when corrupted data is detected.

## Features

• Upload dental images with `.json` metadata files  
• Automatic validation of metadata (e.g., patient ID, image type, date)  
• Valid files are stored in DynamoDB  
• Invalid or corrupted files are moved to a quarantine S3 bucket  
• Email alerts are sent via AWS SNS for corrupted data  
• Uses AWS Lambda, S3, DynamoDB, SNS, and Boto3  
• Secure credential handling via `.env` configuration

## Example Metadata (`scan1.json`)

```json
{
  "patient_id": "DENT00123",
  "image_type": "Intraoral",
  "tooth_number": "18",
  "date": "2025-07-17",
  "dentist": "Dr. A. Sharma",
  "notes": "Signs of decay in molar"
}
