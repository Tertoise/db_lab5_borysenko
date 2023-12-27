-- 1. Вивести всі регіони і кількість карт в кожному
CREATE VIEW total_cards_region AS
SELECT
    region.region_name,
    count(distinct region_units.unit_id) +
    count(distinct region_spells.spell_id) +
    count(distinct champion_region.champion_name) as total_cards
FROM
    region
LEFT JOIN region_units ON region.region_name = region_units.region_name
LEFT JOIN region_spells ON region.region_name = region_spells.region_name
LEFT JOIN champion_region ON region.region_name = champion_region.region_name
GROUP BY
    region.region_name;


-- 2. Вивести кількість карт для кожної вартості
CREATE VIEW card_costs AS
SELECT
    card_cost.cost AS card_cost,
    count(*) AS total_cards
FROM
    (
        SELECT cost FROM unit_card
        UNION
        SELECT cost FROM spell_card
        UNION
        SELECT cost FROM champion_card
    ) AS card_cost
LEFT JOIN unit_card ON card_cost.cost = unit_card.cost
LEFT JOIN spell_card ON card_cost.cost = spell_card.cost
LEFT JOIN champion_card ON card_cost.cost = champion_card.cost
GROUP BY
    card_cost.cost
ORDER BY
    card_cost.cost;

-- 3. Вивести залежність атаки юніта від його вартості
CREATE VIEW attack_unit AS
SELECT
    u.cost,
    ROUND(AVG(u.attack), 1) AS average_attack
FROM
    (
        SELECT attack, cost FROM unit_card
        UNION
        SELECT attack, cost FROM champion_card
    ) AS u
GROUP BY
    u.cost
ORDER BY
    u.cost;