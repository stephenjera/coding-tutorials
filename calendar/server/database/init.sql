CREATE TABLE IF NOT EXISTS "events" (
    "id" INTEGER,
    "start" TIMESTAMP,
    "end" TIMESTAMP,
    "startStr" text,
    "endStr" text,
    "allDay" BOOLEAN,
    PRIMARY KEY ("id")
);