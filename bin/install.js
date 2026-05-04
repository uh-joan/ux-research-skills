#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const os = require('os');

const SKILLS = [
  'empathy-map-generator',
  'empathy-clustering',
  'user-journey',
  'persona-generator',
  'jtbd-analyzer',
  'scenario-mapper',
  'ai-opportunity-analyzer',
  'journey-figma-creator',
];

const args = process.argv.slice(2);
const projectMode = args.includes('--project');

const targetBase = projectMode
  ? path.join(process.cwd(), '.claude', 'skills')
  : path.join(os.homedir(), '.claude', 'skills');

const sourceBase = path.join(__dirname, '..', '.claude', 'skills');

const scope = projectMode ? 'project (.claude/skills/)' : 'global (~/.claude/skills/)';
console.log(`\nInstalling UX Research Skills → ${scope}\n`);

function copyDir(src, dest) {
  fs.mkdirSync(dest, { recursive: true });
  for (const entry of fs.readdirSync(src, { withFileTypes: true })) {
    const srcPath = path.join(src, entry.name);
    const destPath = path.join(dest, entry.name);
    if (entry.isDirectory()) {
      copyDir(srcPath, destPath);
    } else {
      fs.copyFileSync(srcPath, destPath);
    }
  }
}

let installed = 0;
for (const skill of SKILLS) {
  const src = path.join(sourceBase, skill);
  const dest = path.join(targetBase, skill);
  if (!fs.existsSync(src)) {
    console.warn(`  ⚠  Skipping ${skill} (not found in package)`);
    continue;
  }
  copyDir(src, dest);
  console.log(`  ✓  ${skill}`);
  installed++;
}

console.log(`\n${installed} skill${installed !== 1 ? 's' : ''} installed.`);
console.log('Restart Claude Code to activate them, then type /empathy-map-generator to get started.\n');
