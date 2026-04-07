#!/usr/bin/env node

/**
 * Jobs-to-be-Done Analyzer
 *
 * Extracts structured JTBD statements from interview transcripts using LLM pattern recognition.
 *
 * Framework: Clayton Christensen (Harvard, 2005) → Bob Moesta refinement
 * Structure: When [context] → I want to [motivation] → So I can [outcome]
 *
 * Usage:
 *   node index.js <transcript-path> [options]
 *
 * Options:
 *   --journey <path>    Cross-reference with journey map file
 *   --persona <name>    Persona name for output
 *   --output <path>     Output file path (default: DI&A/jtbd/)
 */

const fs = require('fs');
const path = require('path');

// Helper: Read file
function readFile(filePath) {
  try {
    return fs.readFileSync(filePath, 'utf-8');
  } catch (error) {
    console.error(`❌ Error reading file: ${filePath}`);
    console.error(error.message);
    process.exit(1);
  }
}

// Helper: Write file
function writeFile(filePath, content) {
  try {
    const dir = path.dirname(filePath);
    if (!fs.existsSync(dir)) {
      fs.mkdirSync(dir, { recursive: true });
    }
    fs.writeFileSync(filePath, content, 'utf-8');
    console.log(`✅ Output written to: ${filePath}`);
  } catch (error) {
    console.error(`❌ Error writing file: ${filePath}`);
    console.error(error.message);
    process.exit(1);
  }
}

// Parse command line arguments
function parseArgs() {
  const args = process.argv.slice(2);

  if (args.length === 0 || args[0] === '--help') {
    console.log(`
Jobs-to-be-Done Analyzer

Usage:
  node index.js <transcript-path> [options]

Options:
  --journey <path>    Cross-reference with journey map file
  --persona <name>    Persona name for output
  --output <path>     Output file path (default: DI&A/jtbd/)
  --help              Show this help message

Examples:
  node index.js DI&A/transcripts/henok.txt
  node index.js DI&A/transcripts/henok.txt --persona "Dr. Sarah Mitchell"
  node index.js DI&A/transcripts/henok.txt --journey DI&A/journey/user-journey-henok.md
    `);
    process.exit(0);
  }

  const config = {
    transcriptPath: args[0],
    journeyPath: null,
    personaName: null,
    outputPath: null
  };

  for (let i = 1; i < args.length; i += 2) {
    const flag = args[i];
    const value = args[i + 1];

    switch (flag) {
      case '--journey':
        config.journeyPath = value;
        break;
      case '--persona':
        config.personaName = value;
        break;
      case '--output':
        config.outputPath = value;
        break;
      default:
        console.error(`❌ Unknown flag: ${flag}`);
        process.exit(1);
    }
  }

  // Set default output path
  if (!config.outputPath) {
    const filename = path.basename(config.transcriptPath, path.extname(config.transcriptPath));
    config.outputPath = `DI&A/jtbd/jtbd-analysis-${filename}.md`;
  }

  return config;
}

// Main function (to be implemented with Claude)
async function main() {
  console.log('🎯 Jobs-to-be-Done Analyzer');
  console.log('');

  const config = parseArgs();

  console.log('📄 Reading transcript:', config.transcriptPath);
  const transcript = readFile(config.transcriptPath);

  let journeyMap = null;
  if (config.journeyPath) {
    console.log('📊 Reading journey map:', config.journeyPath);
    journeyMap = readFile(config.journeyPath);
  }

  console.log('');
  console.log('🤖 Analyzing Jobs-to-be-Done with Claude...');
  console.log('');

  // This is where Claude will do the actual analysis
  // The analysis will be done via the SKILL.md instructions
  console.log('⚠️  This script is a placeholder.');
  console.log('    The actual JTBD analysis should be run via Claude Code using the skill.');
  console.log('');
  console.log('📝 To run the analysis, use:');
  console.log('    "Analyze jobs-to-be-done from ' + config.transcriptPath + '"');
  console.log('');

  process.exit(0);
}

// Run if called directly
if (require.main === module) {
  main().catch(error => {
    console.error('❌ Fatal error:', error.message);
    process.exit(1);
  });
}

module.exports = { readFile, writeFile, parseArgs };
