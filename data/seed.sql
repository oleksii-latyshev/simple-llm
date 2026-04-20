CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    category VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    description TEXT
);

CREATE TABLE IF NOT EXISTS feedback (
    id SERIAL PRIMARY KEY,
    product_id INTEGER NOT NULL REFERENCES products(id),
    author VARCHAR(100) NOT NULL,
    rating INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5),
    comment TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Products
INSERT INTO products (name, category, price, description) VALUES
('Sony WH-1000XM5',       'Headphones', 349.99, 'Wireless noise-cancelling over-ear headphones'),
('Apple AirPods Pro 2',   'Headphones', 249.99, 'In-ear wireless headphones with ANC'),
('Samsung Galaxy S24',    'Smartphones', 799.99, 'Flagship smartphone with AI features'),
('Kindle Paperwhite',     'E-readers',  139.99, 'Waterproof e-reader with warm light'),
('Logitech MX Master 3S', 'Peripherals', 99.99, 'Ergonomic wireless mouse for productivity');

-- Feedback for Sony WH-1000XM5
INSERT INTO feedback (product_id, author, rating, comment) VALUES
(1, 'Alice',   5, 'Best noise cancelling I have ever tried. Perfect for flights.'),
(1, 'Bob',     4, 'Sound quality is great, but they get warm after 2 hours of use.'),
(1, 'Charlie', 3, 'Good headphones but the touch controls are too sensitive. I keep accidentally pausing music.'),
(1, 'Diana',   5, 'Upgraded from XM4 — the comfort and ANC are noticeably better.'),
(1, 'Eve',     2, 'They creak when I move my head. Build quality is not great for the price.');

-- Feedback for AirPods Pro 2
INSERT INTO feedback (product_id, author, rating, comment) VALUES
(2, 'Frank',   5, 'Seamless integration with iPhone. ANC is impressive for earbuds.'),
(2, 'Grace',   4, 'Great sound for the size, but they fall out during workouts.'),
(2, 'Hank',    3, 'Good product but the case scratches way too easily.'),
(2, 'Ivy',     4, 'Love the spatial audio feature. Battery life could be better though.');

-- Feedback for Samsung Galaxy S24
INSERT INTO feedback (product_id, author, rating, comment) VALUES
(3, 'Jack',    5, 'The AI photo editing tools are a game changer.'),
(3, 'Karen',   4, 'Excellent display and performance. Camera is top tier.'),
(3, 'Leo',     2, 'Battery barely lasts a day with heavy use. Disappointing.'),
(3, 'Mona',    3, 'Good phone but feels too similar to S23. Not worth upgrading.'),
(3, 'Nick',    4, 'Fast, smooth, great screen. Samsung bloatware is still annoying though.');

-- Feedback for Kindle Paperwhite
INSERT INTO feedback (product_id, author, rating, comment) VALUES
(4, 'Olivia',  5, 'I read every night now. The warm light is perfect before bed.'),
(4, 'Pete',    5, 'Battery lasts weeks. Best purchase this year.'),
(4, 'Quinn',   4, 'Love it, but page turns feel slightly laggy compared to real paper.'),
(4, 'Rose',    3, 'Good device but managing library and sideloading books is painful.');

-- Feedback for Logitech MX Master 3S
INSERT INTO feedback (product_id, author, rating, comment) VALUES
(5, 'Steve',   5, 'Best mouse I have owned. The scroll wheel is incredibly smooth.'),
(5, 'Tina',    4, 'Great ergonomics, my wrist pain is gone. A bit heavy for travel.'),
(5, 'Uma',     4, 'Multi-device switching works flawlessly. Thumb button placement is awkward.'),
(5, 'Victor',  2, 'Bluetooth connection drops constantly on my Linux machine. Frustrating.');
