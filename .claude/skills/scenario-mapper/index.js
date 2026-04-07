#!/usr/bin/env node

/**
 * Scenario Mapper Skill
 *
 * Transforms JTBD analysis into NN/g scenarios and Agile user stories
 * for design exploration and product backlog creation.
 *
 * @see .claude/skills/scenario-mapper/SKILL.md for full documentation
 */

console.log("🎬 Scenario Mapper skill loaded");
console.log("📋 Generating design scenarios and user stories from JTBD analysis...");
console.log("");
console.log("This skill will:");
console.log("  1. Extract high-confidence jobs from JTBD analysis files");
console.log("  2. Convert jobs → NN/g 5-element scenarios (Actor, Motivator, Intention, Action, Resolution)");
console.log("  3. Generate Agile user stories with acceptance criteria");
console.log("  4. Prioritize scenarios using MoSCoW method (Must/Should/Could/Won't)");
console.log("  5. Synthesize cross-scenario design themes");
console.log("  6. Prepare workshop facilitation guide");
console.log("");
console.log("Output: scenario-map-[date].md with prioritized scenarios ready for design sprints");
