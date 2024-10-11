#!/usr/bin/env -S deno run --allow-read --allow-write --no-prompt

import gettextParser from "npm:gettext-parser";
import { sprintf } from "jsr:@std/fmt/printf";

const readFromPo = (poContents) =>
  Object.entries(gettextParser.po.parse(poContents).translations).flatMap(
    ([context, strings]) =>
      Object.values(strings)
        .map(({ msgid, msgstr }) => ({ context, key: msgid, value: msgstr[0] }))
        .filter(({ value }) => Boolean(value)),
  );

const data = Object.fromEntries(
  Deno.readDirSync("po")
    .map((file) => file.name.match(/^(?<lng>.*).po$/)?.groups?.lng)
    .filter((lng) => lng !== undefined)
    .map((lng) => [lng, readFromPo(Deno.readTextFileSync(`po/${lng}.po`))]),
);

const renderString = ({ context, key, value }) =>
  sprintf("(%s, %s): %s", ...[context || '*', key, value].map(JSON.stringify));

Deno.writeTextFileSync(
  "translations.py",
  sprintf(
    "translations_dict = { %s }",
    Object.entries(data)
      .map(([lng, strs]) => `"${lng}": { ${strs.map(renderString).join(",")} }`)
      .join(","),
  ),
);
