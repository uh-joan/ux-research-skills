#!/usr/bin/env node

/**
 * AI Opportunity Analyzer
 *
 * Evaluates and prioritizes AI product opportunities using a three-dimensional framework:
 * User Needs × Business Value × Technical Feasibility
 *
 * Framework:
 * - User Needs: Pain severity, frequency, trust threshold, explainability (from JTBD analysis)
 * - Business Value: Strategic alignment, competitive differentiation, revenue impact, user reach
 * - Technical Feasibility: LLM capability match, data availability, hallucination risk, latency, integration complexity
 *
 * Output: AI Feasibility Matrix (2×2) with Priority 1-4 recommendations
 *
 * Usage:
 *   node index.js [options]
 *
 * Options:
 *   --jtbd-dir <path>      Directory with JTBD analysis files (default: DI&A/jtbd/)
 *   --product-context <path>   Product strategy/context file
 *   --technical-context <path> Technical constraints/capabilities file
 *   --output <path>        Output file path (default: DI&A/ai-opportunities/)
 *   --help                 Show this help message
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

// Helper: Read directory
function readDirectory(dirPath) {
  try {
    return fs.readdirSync(dirPath);
  } catch (error) {
    console.error(`❌ Error reading directory: ${dirPath}`);
    console.error(error.message);
    process.exit(1);
  }
}

// Parse command line arguments
function parseArgs() {
  const args = process.argv.slice(2);

  if (args.includes('--help') || args.length === 0) {
    console.log(`
AI Opportunity Analyzer

Evaluates and prioritizes AI product opportunities using three-dimensional assessment:
- User Needs (pain severity, frequency, trust threshold, explainability)
- Business Value (strategic alignment, competitive differentiation, revenue, reach)
- Technical Feasibility (LLM capability, data availability, hallucination risk, latency, integration)

Usage:
  node index.js [options]

Options:
  --jtbd-dir <path>           Directory with JTBD analysis files (default: DI&A/jtbd/)
  --product-context <path>    Product strategy/context file (optional)
  --technical-context <path>  Technical constraints/capabilities file (optional)
  --output <path>             Output file path (default: DI&A/ai-opportunities/)
  --help                      Show this help message

Examples:
  # Basic usage (uses all JTBD files in DI&A/jtbd/)
  node index.js

  # With custom JTBD directory
  node index.js --jtbd-dir /path/to/jtbd/analyses

  # With product and technical context
  node index.js --product-context docs/product-strategy.md --technical-context docs/tech-stack.md

  # Custom output location
  node index.js --output reports/ai-opportunities-q1-2026.md
    `);
    process.exit(0);
  }

  const config = {
    jtbdDir: 'DI&A/jtbd/',
    productContext: null,
    technicalContext: null,
    outputPath: null
  };

  for (let i = 0; i < args.length; i += 2) {
    const flag = args[i];
    const value = args[i + 1];

    switch (flag) {
      case '--jtbd-dir':
        config.jtbdDir = value;
        break;
      case '--product-context':
        config.productContext = value;
        break;
      case '--technical-context':
        config.technicalContext = value;
        break;
      case '--output':
        config.outputPath = value;
        break;
      default:
        console.error(`❌ Unknown flag: ${flag}`);
        console.error('Use --help for usage information');
        process.exit(1);
    }
  }

  // Set default output path with timestamp
  if (!config.outputPath) {
    const date = new Date().toISOString().split('T')[0];
    config.outputPath = `DI&A/ai-opportunities/ai-opportunity-assessment-${date}.md`;
  }

  return config;
}

// Main function (to be implemented with Claude)
async function main() {
  console.log('🎯 AI Opportunity Analyzer');
  console.log('');

  const config = parseArgs();

  // Validate JTBD directory exists
  if (!fs.existsSync(config.jtbdDir)) {
    console.error(`❌ JTBD directory not found: ${config.jtbdDir}`);
    console.error('Please run JTBD Analyzer skill first or specify valid --jtbd-dir');
    process.exit(1);
  }

  console.log('📂 Reading JTBD analyses from:', config.jtbdDir);
  const jtbdFiles = readDirectory(config.jtbdDir)
    .filter(file => file.endsWith('.md'))
    .filter(file => file.startsWith('jtbd-analysis-'));

  console.log(`   Found ${jtbdFiles.length} JTBD analysis files`);
  console.log('');

  if (config.productContext) {
    console.log('📄 Reading product context:', config.productContext);
    const productContext = readFile(config.productContext);
    console.log('');
  }

  if (config.technicalContext) {
    console.log('🔧 Reading technical context:', config.technicalContext);
    const technicalContext = readFile(config.technicalContext);
    console.log('');
  }

  console.log('🤖 Analyzing AI opportunities with Claude...');
  console.log('');

  // This is where Claude will do the actual analysis
  // The analysis will be done via the SKILL.md instructions
  console.log('⚠️  This script is a placeholder.');
  console.log('    The actual AI opportunity analysis should be run via Claude Code using the skill.');
  console.log('');
  console.log('📝 To run the analysis, use:');
  console.log('    "Analyze AI opportunities from JTBD analysis in ' + config.jtbdDir + '"');
  console.log('');
  console.log('💡 The skill will:');
  console.log('   1. Extract AI opportunity candidates from JTBD files');
  console.log('   2. Score each opportunity across 3 dimensions (User Needs, Business Value, Technical Feasibility)');
  console.log('   3. Map to AI Feasibility Matrix (Priority 1-4)');
  console.log('   4. Generate prioritization recommendations');
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

module.exports = { readFile, writeFile, readDirectory, parseArgs };
