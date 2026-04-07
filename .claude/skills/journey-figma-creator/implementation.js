/**
 * User Journey Mapper - Figma Code Implementation
 *
 * This file contains the reusable Figma code for creating journey maps
 * from parsed markdown data. Use this as a reference when implementing
 * the user-journey-mapper skill.
 *
 * Usage: Copy relevant sections into figma_execute calls
 */

// ============================================================================
// PART 1: PARSE MARKDOWN STRUCTURE
// ============================================================================
// (This happens in Claude Code using Read tool and text parsing)
// Expected data structure:

const exampleParsedData = {
  title: "Annual Product Forecasting Workflow",
  actor: {
    name: "Han, Shirley",
    role: "Market & Commercial Research Analyst (MCRA)",
    organization: "Marketing Engagement Excellence team",
    team: "4-person team covering different therapeutic areas",
    responsibilities: [
      "Long-range forecasting (LRFP) for pipeline products",
      "Performance tracking for in-market products"
    ]
  },
  scenario: {
    goal: "Create accurate annual long-range forecasts",
    context: "Annual LRFP cycle where regional team receives global guidance",
    expectations: [
      "Receive reliable, Canada-specific data",
      "Build defensible forecasts"
    ]
  },
  phases: [
    {
      name: "Receive Global Guidance",
      timeline: "Annual cycle kickoff",
      actions: [
        "Receive guidance from global team",
        "Review global demo study results"
      ],
      mindsets: [
        "How do these global assumptions apply to Canada?",
        "What data can I use as a starting point?"
      ],
      quote: "So from a regional perspective, we will receive guidance from the global team like they will tell, but they will indicate the most important countries like US, EU5, Japan and China.",
      emotions: {
        description: "Neutral to slightly overwhelmed",
        rating: 2
      },
      painPoints: [
        "Global guidance focuses on major markets, not Canada",
        "Limited Canada-specific data"
      ],
      dataSources: ["Global guidance book", "Demo study results"],
      tools: ["Email", "Global guidance docs"]
    }
    // ... more phases
  ],
  opportunities: [
    {
      name: "Canada-Specific Epidemiological Data",
      issue: "Limited Canada-specific data forces reliance on assumptions",
      impact: "Reduces forecast confidence and defensibility",
      metric: "% of forecasts with Canada sources",
      quote: "If they have the Canada specific data, we will buy it"
    }
    // ... more opportunities
  ]
};

// ============================================================================
// PART 2: CREATE FIGMA JOURNEY MAP STRUCTURE
// ============================================================================

async function createJourneyMapStructure(parsedData) {
  // Load fonts
  await figma.loadFontAsync({ family: "Inter", style: "Bold" });
  await figma.loadFontAsync({ family: "Inter", style: "Regular" });
  await figma.loadFontAsync({ family: "Inter", style: "Medium" });
  await figma.loadFontAsync({ family: "Inter", style: "Semi Bold" });

  // Create main Section
  const mainSection = figma.createSection();
  mainSection.name = `${parsedData.actor.name}'s Journey Map`;
  mainSection.x = 100;
  mainSection.y = 100;

  const numPhases = parsedData.phases.length;
  const totalWidth = 40 + (numPhases * 960) + 40;
  mainSection.resizeWithoutConstraints(totalWidth, 2000);
  figma.currentPage.appendChild(mainSection);

  // Create main frame
  const journeyFrame = figma.createFrame();
  journeyFrame.name = `Journey Map - ${parsedData.actor.name}`;
  journeyFrame.x = 150;
  journeyFrame.y = 150;
  journeyFrame.resizeWithoutConstraints(totalWidth - 100, 1800);
  journeyFrame.fills = [{type: 'SOLID', color: {r: 1, g: 1, b: 1}}];
  mainSection.appendChild(journeyFrame);

  return { journeyFrame, totalWidth };
}

// ============================================================================
// PART 3: ADD TITLE AND HEADER
// ============================================================================

function addHeader(journeyFrame, parsedData) {
  // Title
  const title = figma.createText();
  title.fontName = { family: "Inter", style: "Bold" };
  title.fontSize = 48;
  title.characters = `${parsedData.actor.name}'s ${parsedData.title}`;
  title.x = 40;
  title.y = 40;
  title.fills = [{type: 'SOLID', color: {r: 0, g: 0, b: 0}}];
  journeyFrame.appendChild(title);

  // Subtitle
  const subtitle = figma.createText();
  subtitle.fontName = { family: "Inter", style: "Regular" };
  subtitle.fontSize = 16;
  subtitle.characters = `${parsedData.actor.role} - ${parsedData.actor.organization}`;
  subtitle.x = 40;
  subtitle.y = 100;
  subtitle.fills = [{type: 'SOLID', color: {r: 0.4, g: 0.4, b: 0.4}}];
  journeyFrame.appendChild(subtitle);
}

// ============================================================================
// PART 4: PHASE COLOR PALETTE
// ============================================================================

const phaseColors = [
  {r: 0.9, g: 0.95, b: 1},    // Light blue
  {r: 0.85, g: 0.95, b: 0.85}, // Light green
  {r: 1, g: 0.95, b: 0.85},    // Light orange
  {r: 0.95, g: 0.9, b: 1},     // Light purple
  {r: 1, g: 0.9, b: 0.9},      // Light pink
  {r: 0.95, g: 0.95, b: 0.85}  // Light yellow
];

function getPhaseColor(index) {
  return phaseColors[index % phaseColors.length];
}

// ============================================================================
// PART 5: CREATE PHASE HEADERS
// ============================================================================

function createPhaseHeaders(journeyFrame, parsedData) {
  parsedData.phases.forEach((phase, index) => {
    const phaseX = 40 + (index * 960);

    const phaseFrame = figma.createFrame();
    phaseFrame.name = phase.name;
    phaseFrame.x = phaseX;
    phaseFrame.y = 160;
    phaseFrame.resizeWithoutConstraints(920, 120);
    phaseFrame.fills = [{type: 'SOLID', color: getPhaseColor(index)}];
    phaseFrame.cornerRadius = 8;
    journeyFrame.appendChild(phaseFrame);

    const phaseTitle = figma.createText();
    phaseTitle.fontName = { family: "Inter", style: "Semi Bold" };
    phaseTitle.fontSize = 20;
    phaseTitle.characters = phase.name;
    phaseTitle.x = 20;
    phaseTitle.y = 20;
    phaseTitle.fills = [{type: 'SOLID', color: {r: 0, g: 0, b: 0}}];
    phaseFrame.appendChild(phaseTitle);
  });
}

// ============================================================================
// PART 6: ADD PHASE CONTENT (TRIGGERS, ACTIONS, DATA SOURCES)
// ============================================================================

function addPhaseContent(journeyFrame, parsedData) {
  let baseY = 320;

  parsedData.phases.forEach((phase, index) => {
    const phaseX = 40 + (index * 960);
    let currentY = baseY;

    // Trigger card
    const triggerLabel = figma.createFrame();
    triggerLabel.name = "Trigger";
    triggerLabel.x = phaseX;
    triggerLabel.y = currentY;
    triggerLabel.resizeWithoutConstraints(920, 50);
    triggerLabel.fills = [{type: 'SOLID', color: {r: 1, g: 0.98, b: 0.9}}];
    triggerLabel.cornerRadius = 4;
    journeyFrame.appendChild(triggerLabel);

    const triggerText = figma.createText();
    triggerText.fontName = { family: "Inter", style: "Medium" };
    triggerText.fontSize = 12;
    triggerText.characters = `Trigger: ${phase.timeline}`;
    triggerText.x = 10;
    triggerText.y = 10;
    triggerText.fills = [{type: 'SOLID', color: {r: 0.6, g: 0.4, b: 0}}];
    triggerLabel.appendChild(triggerText);

    const emotionText = figma.createText();
    emotionText.fontName = { family: "Inter", style: "Regular" };
    emotionText.fontSize = 10;
    emotionText.characters = `Emotion: ${phase.emotions.description} (${phase.emotions.rating}/5)`;
    emotionText.x = 10;
    emotionText.y = 28;
    emotionText.fills = [{type: 'SOLID', color: {r: 0.5, g: 0.5, b: 0.5}}];
    triggerLabel.appendChild(emotionText);

    currentY += 60;

    // Quote card (if quote exists)
    if (phase.quote) {
      const quoteCard = figma.createFrame();
      quoteCard.name = "Quote";
      quoteCard.x = phaseX;
      quoteCard.y = currentY;
      quoteCard.resizeWithoutConstraints(920, 80);
      quoteCard.fills = [{type: 'SOLID', color: {r: 0.98, g: 0.98, b: 1}}];
      quoteCard.cornerRadius = 6;
      quoteCard.strokeWeight = 2;
      quoteCard.strokes = [{type: 'SOLID', color: {r: 0.7, g: 0.7, b: 0.9}}];
      journeyFrame.appendChild(quoteCard);

      const quoteIcon = figma.createText();
      quoteIcon.fontName = { family: "Inter", style: "Bold" };
      quoteIcon.fontSize = 16;
      quoteIcon.characters = '"';
      quoteIcon.x = 12;
      quoteIcon.y = 10;
      quoteIcon.fills = [{type: 'SOLID', color: {r: 0.4, g: 0.4, b: 0.7}}];
      quoteCard.appendChild(quoteIcon);

      const quoteText = figma.createText();
      quoteText.fontName = { family: "Inter", style: "Regular" };
      quoteText.fontSize = 10;
      quoteText.characters = phase.quote;
      quoteText.x = 30;
      quoteText.y = 10;
      quoteText.resize(880, 60);
      quoteText.fills = [{type: 'SOLID', color: {r: 0.3, g: 0.3, b: 0.5}}];
      quoteCard.appendChild(quoteText);

      currentY += 90;
    }

    // Actions label
    const actionsLabel = figma.createText();
    actionsLabel.fontName = { family: "Inter", style: "Semi Bold" };
    actionsLabel.fontSize = 14;
    actionsLabel.characters = "Actions:";
    actionsLabel.x = phaseX;
    actionsLabel.y = currentY;
    actionsLabel.fills = [{type: 'SOLID', color: {r: 0, g: 0, b: 0}}];
    journeyFrame.appendChild(actionsLabel);

    currentY += 30;

    // Action items (limit to first 4 for space)
    phase.actions.slice(0, 4).forEach((action) => {
      const actionCard = figma.createFrame();
      actionCard.name = "Action";
      actionCard.x = phaseX;
      actionCard.y = currentY;
      actionCard.resizeWithoutConstraints(920, 40);
      actionCard.fills = [{type: 'SOLID', color: {r: 0.95, g: 0.98, b: 0.95}}];
      actionCard.cornerRadius = 4;
      actionCard.strokeWeight = 1;
      actionCard.strokes = [{type: 'SOLID', color: {r: 0.8, g: 0.9, b: 0.8}}];
      journeyFrame.appendChild(actionCard);

      const actionText = figma.createText();
      actionText.fontName = { family: "Inter", style: "Regular" };
      actionText.fontSize = 11;
      actionText.characters = `• ${action}`;
      actionText.x = 10;
      actionText.y = 12;
      actionText.fills = [{type: 'SOLID', color: {r: 0.2, g: 0.2, b: 0.2}}];
      actionCard.appendChild(actionText);

      currentY += 45;
    });

    // Data sources
    if (phase.dataSources && phase.dataSources.length > 0) {
      currentY += 10;

      const dataLabel = figma.createText();
      dataLabel.fontName = { family: "Inter", style: "Semi Bold" };
      dataLabel.fontSize = 12;
      dataLabel.characters = "Data Sources:";
      dataLabel.x = phaseX;
      dataLabel.y = currentY;
      dataLabel.fills = [{type: 'SOLID', color: {r: 0.3, g: 0.3, b: 0.7}}];
      journeyFrame.appendChild(dataLabel);

      currentY += 25;

      const dataText = figma.createText();
      dataText.fontName = { family: "Inter", style: "Regular" };
      dataText.fontSize = 10;
      dataText.characters = phase.dataSources.join(", ");
      dataText.x = phaseX;
      dataText.y = currentY;
      dataText.fills = [{type: 'SOLID', color: {r: 0.4, g: 0.4, b: 0.6}}];
      dataText.resize(900, dataText.height);
      journeyFrame.appendChild(dataText);
    }
  });
}

// ============================================================================
// PART 7: ADD PAIN POINTS ROW
// ============================================================================

function addPainPoints(journeyFrame, parsedData) {
  const painPointsY = 900;

  // Header
  const painPointsHeader = figma.createFrame();
  painPointsHeader.name = "Pain Points Header";
  painPointsHeader.x = 40;
  painPointsHeader.y = painPointsY;
  painPointsHeader.resizeWithoutConstraints(parsedData.phases.length * 960, 50);
  painPointsHeader.fills = [{type: 'SOLID', color: {r: 1, g: 0.85, b: 0.85}}];
  painPointsHeader.cornerRadius = 8;
  journeyFrame.appendChild(painPointsHeader);

  const painPointsTitle = figma.createText();
  painPointsTitle.fontName = { family: "Inter", style: "Bold" };
  painPointsTitle.fontSize = 18;
  painPointsTitle.characters = "Pain Points";
  painPointsTitle.x = 20;
  painPointsTitle.y = 15;
  painPointsTitle.fills = [{type: 'SOLID', color: {r: 0.6, g: 0, b: 0}}];
  painPointsHeader.appendChild(painPointsTitle);

  // Pain point cards for each phase
  let currentY = painPointsY + 60;

  parsedData.phases.forEach((phase, index) => {
    const phaseX = 40 + (index * 960);
    let yOffset = currentY;

    phase.painPoints.forEach((painPoint) => {
      const painCard = figma.createFrame();
      painCard.name = "Pain Point";
      painCard.x = phaseX;
      painCard.y = yOffset;
      painCard.resizeWithoutConstraints(920, 50);
      painCard.fills = [{type: 'SOLID', color: {r: 1, g: 0.95, b: 0.95}}];
      painCard.cornerRadius = 4;
      painCard.strokeWeight = 2;
      painCard.strokes = [{type: 'SOLID', color: {r: 0.9, g: 0.3, b: 0.3}}];
      journeyFrame.appendChild(painCard);

      const painText = figma.createText();
      painText.fontName = { family: "Inter", style: "Regular" };
      painText.fontSize = 10;
      painText.characters = `⚠ ${painPoint}`;
      painText.x = 10;
      painText.y = 8;
      painText.resize(900, 40);
      painText.fills = [{type: 'SOLID', color: {r: 0.6, g: 0, b: 0}}];
      painCard.appendChild(painText);

      yOffset += 55;
    });
  });
}

// ============================================================================
// PART 8: ADD TOOLS ROW
// ============================================================================

function addTools(journeyFrame, parsedData) {
  const toolsY = 1450;

  // Header
  const toolsHeader = figma.createFrame();
  toolsHeader.name = "Tools Header";
  toolsHeader.x = 40;
  toolsHeader.y = toolsY;
  toolsHeader.resizeWithoutConstraints(parsedData.phases.length * 960, 40);
  toolsHeader.fills = [{type: 'SOLID', color: {r: 0.9, g: 0.95, b: 1}}];
  toolsHeader.cornerRadius = 8;
  journeyFrame.appendChild(toolsHeader);

  const toolsTitle = figma.createText();
  toolsTitle.fontName = { family: "Inter", style: "Bold" };
  toolsTitle.fontSize = 16;
  toolsTitle.characters = "Tools & Systems";
  toolsTitle.x = 20;
  toolsTitle.y = 10;
  toolsTitle.fills = [{type: 'SOLID', color: {r: 0.2, g: 0.3, b: 0.6}}];
  toolsHeader.appendChild(toolsTitle);

  // Tool cards
  let toolsCurrentY = toolsY + 50;

  parsedData.phases.forEach((phase, index) => {
    if (!phase.tools || phase.tools.length === 0) return;

    const phaseX = 40 + (index * 960);

    const toolsCard = figma.createFrame();
    toolsCard.name = "Tools";
    toolsCard.x = phaseX;
    toolsCard.y = toolsCurrentY;
    toolsCard.resizeWithoutConstraints(920, 60);
    toolsCard.fills = [{type: 'SOLID', color: {r: 0.95, g: 0.97, b: 1}}];
    toolsCard.cornerRadius = 4;
    toolsCard.strokeWeight = 1;
    toolsCard.strokes = [{type: 'SOLID', color: {r: 0.7, g: 0.8, b: 0.95}}];
    journeyFrame.appendChild(toolsCard);

    const toolsText = figma.createText();
    toolsText.fontName = { family: "Inter", style: "Regular" };
    toolsText.fontSize = 10;
    toolsText.characters = phase.tools.join(" • ");
    toolsText.x = 10;
    toolsText.y = 10;
    toolsText.resize(900, 40);
    toolsText.fills = [{type: 'SOLID', color: {r: 0.3, g: 0.4, b: 0.6}}];
    toolsCard.appendChild(toolsText);
  });
}

// ============================================================================
// PART 9: ADD CONTEXT BOXES
// ============================================================================

function addContextBoxes(journeyFrame, parsedData) {
  const boxY = 1600;

  // Context & User Profile
  const contextBox = figma.createFrame();
  contextBox.name = "Context & User Profile";
  contextBox.x = 40;
  contextBox.y = boxY;
  contextBox.resizeWithoutConstraints(1800, 150);
  contextBox.fills = [{type: 'SOLID', color: {r: 0.98, g: 0.99, b: 1}}];
  contextBox.cornerRadius = 8;
  contextBox.strokeWeight = 2;
  contextBox.strokes = [{type: 'SOLID', color: {r: 0.6, g: 0.7, b: 0.9}}];
  journeyFrame.appendChild(contextBox);

  const contextTitle = figma.createText();
  contextTitle.fontName = { family: "Inter", style: "Bold" };
  contextTitle.fontSize = 16;
  contextTitle.characters = "Context & User Profile";
  contextTitle.x = 20;
  contextTitle.y = 15;
  contextTitle.fills = [{type: 'SOLID', color: {r: 0.2, g: 0.3, b: 0.6}}];
  contextBox.appendChild(contextTitle);

  const contextContent = figma.createText();
  contextContent.fontName = { family: "Inter", style: "Regular" };
  contextContent.fontSize = 11;
  contextContent.characters = `Role: ${parsedData.actor.role}
Team: ${parsedData.actor.team}
Organization: ${parsedData.actor.organization}
Key Responsibilities: ${parsedData.actor.responsibilities.join(", ")}`;
  contextContent.x = 20;
  contextContent.y = 45;
  contextContent.resize(1760, 90);
  contextContent.fills = [{type: 'SOLID', color: {r: 0.3, g: 0.3, b: 0.3}}];
  contextBox.appendChild(contextContent);

  // Opportunity Areas (if present)
  if (parsedData.opportunities && parsedData.opportunities.length > 0) {
    const oppBox = figma.createFrame();
    oppBox.name = "Opportunity Areas";
    oppBox.x = 1880;
    oppBox.y = boxY;
    oppBox.resizeWithoutConstraints(2000, 150);
    oppBox.fills = [{type: 'SOLID', color: {r: 1, g: 0.98, b: 0.95}}];
    oppBox.cornerRadius = 8;
    oppBox.strokeWeight = 2;
    oppBox.strokes = [{type: 'SOLID', color: {r: 0.9, g: 0.7, b: 0.3}}];
    journeyFrame.appendChild(oppBox);

    const oppTitle = figma.createText();
    oppTitle.fontName = { family: "Inter", style: "Bold" };
    oppTitle.fontSize = 16;
    oppTitle.characters = "Key Opportunities";
    oppTitle.x = 20;
    oppTitle.y = 15;
    oppTitle.fills = [{type: 'SOLID', color: {r: 0.7, g: 0.4, b: 0}}];
    oppBox.appendChild(oppTitle);

    const oppList = parsedData.opportunities.slice(0, 3).map((opp, idx) =>
      `${idx + 1}. ${opp.name}: ${opp.issue}`
    ).join("\n");

    const oppContent = figma.createText();
    oppContent.fontName = { family: "Inter", style: "Regular" };
    oppContent.fontSize = 11;
    oppContent.characters = oppList;
    oppContent.x = 20;
    oppContent.y = 45;
    oppContent.resize(1960, 90);
    oppContent.fills = [{type: 'SOLID', color: {r: 0.5, g: 0.3, b: 0}}];
    oppBox.appendChild(oppContent);
  }
}

// ============================================================================
// PART 10: MAIN EXECUTION FUNCTION
// ============================================================================

async function createCompleteJourneyMap(parsedData) {
  const { journeyFrame, totalWidth } = await createJourneyMapStructure(parsedData);

  addHeader(journeyFrame, parsedData);
  createPhaseHeaders(journeyFrame, parsedData);
  addPhaseContent(journeyFrame, parsedData);
  addPainPoints(journeyFrame, parsedData);
  addTools(journeyFrame, parsedData);
  addContextBoxes(journeyFrame, parsedData);

  return {
    success: true,
    frameId: journeyFrame.id,
    totalWidth: totalWidth,
    message: "Journey map created successfully"
  };
}

// Export for reference (not actually executable in this file)
// This is documentation code showing the complete implementation
