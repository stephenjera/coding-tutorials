--reate database "events_db";
-- CREATE TABLE IF NOT EXISTS "events" (
--     "id" INTEGER,
--     "start" TIMESTAMP,
--     "end" TIMESTAMP,
--     "startStr" text,
--     "endStr" text,
--     "allDay" BOOLEAN,
--     PRIMARY KEY ("id")
-- );

CREATE TABLE IF NOT EXISTS "events" (
    "id" serial,
    "event" json,
    PRIMARY KEY ("id")
);
