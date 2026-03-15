DROP TABLE IF EXISTS kev;
DROP TABLE IF EXISTS profile_company;
DROP TABLE IF EXISTS profile;
DROP TABLE IF EXISTS company;
DROP TABLE IF EXISTS user;


CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE profile (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  first_name TEXT,
  last_name TEXT,
  display_name TEXT,
  bio TEXT,
  avatar_url TEXT,
  location TEXT,
  website TEXT,
  FOREIGN KEY (user_id) REFERENCES user (id)
);
CREATE TABLE company (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  company_name TEXT NOT NULL UNIQUE
);
CREATE TABLE profile_company (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  profile_id INTEGER NOT NULL,
  company_id INTEGER NOT NULL,
  FOREIGN KEY (profile_id) REFERENCES profile (id),
  FOREIGN KEY (company_id) REFERENCES company (id),
  UNIQUE (profile_id, company_id)
);
CREATE TABLE kev (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  company_id INTEGER NOT NULL,
  cve_id TEXT NOT NULL UNIQUE,        -- e.g. "CVE-2024-1234" (missing!)
  vendor_project TEXT NOT NULL,
  product TEXT,
  vulnerability_name TEXT,            -- short human readable name (missing!)
  date_added TEXT,                    -- when CISA added it to KEV (missing!)
  short_description TEXT,             -- plain English description (missing!)
  required_action TEXT,               -- what to do about it (missing!)
  due_date TEXT,                      -- federal patch deadline (missing!)
  is_active INTEGER NOT NULL DEFAULT 1,
  FOREIGN KEY (company_id) REFERENCES company (id),
  UNIQUE (company_id, cve_id)         -- unique on cve_id not vendor_project
);
CREATE TABLE IF NOT EXISTS tracked_companies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    vendor_name TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES user (id),
    UNIQUE (user_id, vendor_name)
);