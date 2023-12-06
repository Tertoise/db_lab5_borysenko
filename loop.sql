-- Додаємо 2 нові карти в регіон Shadow Isles
DO $$ 
DECLARE
    i INT;
BEGIN
    FOR i IN 1..2 LOOP
        INSERT INTO spell_card (cost, effect, name, spell_id)
        VALUES (
            3,
            CASE i
                WHEN 1 THEN 'Kill an ally to deal 5'
                WHEN 2 THEN 'Grant an ally Deathless'
            END,
            CASE i
                WHEN 1 THEN 'Death''s grasp'
                WHEN 2 THEN 'Indestructible'
            END,
            CASE i
                WHEN 1 THEN '2sis'
                WHEN 2 THEN '3sis'
            END
        );
    END LOOP;
END $$;

select * from spell_card