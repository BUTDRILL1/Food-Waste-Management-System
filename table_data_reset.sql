-- Provider Reset
SELECT * FROM providers ORDER BY provider_id DESC LIMIT 3;
DELETE FROM providers WHERE provider_id > 1000;
SELECT setval('providers_provider_id_seq', 1000, false);
SELECT column_default FROM information_schema.columns WHERE table_name = 'providers' AND column_name = 'provider_id';

-- Receiver Reset
SELECT * FROM receivers ORDER BY receiver_id DESC LIMIT 3;
DELETE FROM receivers WHERE receiver_id > 1000;
SELECT setval('receivers_receiver_id_seq', 1000, false);
SELECT column_default FROM information_schema.columns WHERE table_name = 'receivers' AND column_name = 'receiver_id';

-- Food Listing Reset
SELECT * FROM food_listings ORDER BY food_id DESC LIMIT 3;
DELETE FROM food_listings WHERE food_id > 1000;
SELECT setval('food_listings_food_id_seq', 1000, false);
SELECT column_default FROM information_schema.columns WHERE table_name = 'food_listings' AND column_name = 'food_id';

-- Claim Reset
SELECT * FROM claims ORDER BY claim_id DESC LIMIT 3;
DELETE FROM claims WHERE claim_id > 1000;
SELECT setval('claims_claim_id_seq', 1000, false);
SELECT column_default FROM information_schema.columns WHERE table_name = 'claims' AND column_name = 'claim_id';