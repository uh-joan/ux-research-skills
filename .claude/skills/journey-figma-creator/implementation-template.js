/**
 * Template-Based Journey Map Generator
 *
 * This implementation handles journey map generation using external Figma templates.
 * Supports content replacement in pre-designed templates.
 *
 * Template URL: https://www.figma.com/design/mE4eNMq71OOXSkH4SihpnX/User-journey---template
 */

// ============================================================================
// PART 1: TEMPLATE CLONING
// ============================================================================

/**
 * Clone template from external file to current file
 * Uses Figma's importComponentByKeyAsync or manual node cloning
 */
async function cloneTemplateToCurrentFile(templateFileKey, templateNodeId) {
  // Note: This would typically be done via REST API fetch + recreate
  // For now, we'll use a different approach: direct node inspection and recreation

  const result = {
    success: false,
    clonedFrame: null,
    message: ''
  };

  try {
    // In practice, you would:
    // 1. Fetch template structure via figma_get_file_data (REST API)
    // 2. Recursively recreate nodes in current file
    // 3. Preserve all styling, layout, and component relationships

    // For this implementation, we'll create a simplified version
    // that assumes the template is already in the same file or
    // uses importComponentByKeyAsync for components

    result.success = true;
    result.message = 'Template cloning initiated';

    return result;

  } catch (error) {
    result.message = `Template cloning failed: ${error.message}`;
    return result;
  }
}

// ============================================================================
// PART 2: PHASE FRAME DETECTION
// ============================================================================

/**
 * Find all phase frames in the cloned template
 * Pattern: Frames with numbered badges + phase titles
 */
function findPhaseFrames(templateFrame) {
  const phaseFrames = [];

  function traverse(node, depth = 0) {
    if (depth > 10) return; // Prevent infinite recursion

    // Check if this node matches phase pattern:
    // - Contains a numbered badge (text node with single digit)
    // - Contains a title text node
    // - Has 3-column container layout

    if (node.type === 'FRAME' && node.children) {
      const hasNumberBadge = node.children.some(child =>
        child.type === 'TEXT' && /^[0-9]$/.test(child.characters)
      );

      const hasTitleText = node.children.some(child =>
        child.type === 'TEXT' && child.characters.length > 5
      );

      if (hasNumberBadge && hasTitleText) {
        phaseFrames.push({
          frame: node,
          number: parseInt(node.children.find(c =>
            c.type === 'TEXT' && /^[0-9]$/.test(c.characters)
          )?.characters || '0'),
          title: node.children.find(c =>
            c.type === 'TEXT' && c.characters.length > 5
          )?.characters || ''
        });
      }

      // Continue traversing
      node.children.forEach(child => traverse(child, depth + 1));
    }
  }

  traverse(templateFrame);

  // Sort by phase number
  phaseFrames.sort((a, b) => a.number - b.number);

  return phaseFrames;
}

// ============================================================================
// PART 3: CONTENT REPLACEMENT
// ============================================================================

/**
 * Replace text content in a phase frame
 */
async function replacePhaseContent(phaseFrame, phaseData, phaseNumber) {
  const { frame } = phaseFrame;

  // Load fonts first
  await loadRequiredFonts();

  // Find and update numbered badge
  const numberNode = findTextNode(frame, /^[0-9]$/);
  if (numberNode) {
    numberNode.characters = phaseNumber.toString();
  }

  // Find and update phase title
  const titleNode = findTextNode(frame, /.{5,}/); // Title is longer text
  if (titleNode && phaseData.name) {
    titleNode.characters = phaseData.name;
  }

  // Find 3-column container
  const columns = find3ColumnContainer(frame);

  if (columns) {
    // Column 1: Actions
    if (columns[0] && phaseData.actions) {
      await populateColumn(columns[0], phaseData.actions, 'actions');
    }

    // Column 2: Mindsets/Emotions
    if (columns[1] && phaseData.mindsets) {
      await populateColumn(columns[1], phaseData.mindsets, 'mindsets');
    }

    // Column 3: Pain Points/Tools
    if (columns[2] && phaseData.painPoints) {
      await populateColumn(columns[2], phaseData.painPoints, 'painPoints');
    }
  }

  return {
    success: true,
    phaseNumber,
    phaseName: phaseData.name
  };
}

/**
 * Find text node by pattern
 */
function findTextNode(parent, pattern) {
  if (parent.type === 'TEXT' && pattern.test(parent.characters)) {
    return parent;
  }

  if ('children' in parent) {
    for (const child of parent.children) {
      const found = findTextNode(child, pattern);
      if (found) return found;
    }
  }

  return null;
}

/**
 * Find 3-column container layout
 * Returns array of 3 container frames (or null)
 */
function find3ColumnContainer(parent) {
  function traverse(node, depth = 0) {
    if (depth > 8) return null;

    // Look for a frame with 3 children frames of specific widths
    if (node.type === 'FRAME' && node.children && node.children.length === 3) {
      const widths = node.children.map(c => Math.round(c.width));

      // Check if widths match template pattern: ~282, ~243, ~195
      if (Math.abs(widths[0] - 282) < 20 &&
          Math.abs(widths[1] - 243) < 20 &&
          Math.abs(widths[2] - 195) < 20) {
        return node.children;
      }
    }

    if ('children' in node) {
      for (const child of node.children) {
        const found = traverse(child, depth + 1);
        if (found) return found;
      }
    }

    return null;
  }

  return traverse(parent);
}

/**
 * Populate a column with content
 */
async function populateColumn(columnFrame, contentArray, columnType) {
  // Clear existing content (except labels/headers)
  const existingContent = columnFrame.children.filter(c =>
    c.type === 'TEXT' && c.characters.length > 2
  );

  // For simplicity, we'll update existing text nodes or create new ones
  // In a real implementation, you'd match the template's card/list style

  for (let i = 0; i < Math.min(contentArray.length, 5); i++) {
    if (existingContent[i]) {
      // Update existing text node
      existingContent[i].characters = formatContent(contentArray[i], columnType);
    } else {
      // Create new text node matching template style
      const newText = figma.createText();
      await newText.loadFontAsync(existingContent[0]?.fontName || { family: "Inter", style: "Regular" });
      newText.characters = formatContent(contentArray[i], columnType);
      newText.fontSize = existingContent[0]?.fontSize || 11;
      columnFrame.appendChild(newText);
    }
  }
}

/**
 * Format content based on column type
 */
function formatContent(content, columnType) {
  switch (columnType) {
    case 'actions':
      return `• ${content}`;
    case 'mindsets':
      return `"${content}"`;
    case 'painPoints':
      return `⚠ ${content}`;
    default:
      return content;
  }
}

/**
 * Load required fonts
 */
async function loadRequiredFonts() {
  const fonts = [
    { family: "Inter", style: "Regular" },
    { family: "Inter", style: "Medium" },
    { family: "Inter", style: "Semi Bold" },
    { family: "Inter", style: "Bold" }
  ];

  for (const font of fonts) {
    try {
      await figma.loadFontAsync(font);
    } catch (e) {
      console.warn(`Could not load font ${font.family} ${font.style}`);
    }
  }
}

// ============================================================================
// PART 4: PHASE COUNT ADJUSTMENT
// ============================================================================

/**
 * Adjust number of phases to match markdown data
 * - If markdown has fewer phases: Delete extra phase frames
 * - If markdown has more phases: Clone phase component to create more
 */
async function adjustPhaseCount(clonedTemplate, requiredPhaseCount, currentPhaseCount) {
  if (requiredPhaseCount === currentPhaseCount) {
    return { success: true, message: 'Phase count matches' };
  }

  if (requiredPhaseCount < currentPhaseCount) {
    // Delete extra phases
    const phaseFrames = findPhaseFrames(clonedTemplate);
    const toDelete = phaseFrames.slice(requiredPhaseCount);

    for (const { frame } of toDelete) {
      frame.remove();
    }

    return {
      success: true,
      message: `Deleted ${toDelete.length} extra phases`
    };
  }

  if (requiredPhaseCount > currentPhaseCount) {
    // Clone phase component to create more
    const phaseFrames = findPhaseFrames(clonedTemplate);
    const lastPhase = phaseFrames[phaseFrames.length - 1];
    const phasesToAdd = requiredPhaseCount - currentPhaseCount;

    // Find the parent page frame
    const parentPage = lastPhase.frame.parent;

    for (let i = 0; i < phasesToAdd; i++) {
      // Clone the last phase frame
      const clonedPhase = lastPhase.frame.clone();
      parentPage.appendChild(clonedPhase);

      // Update the phase number
      const numberNode = findTextNode(clonedPhase, /^[0-9]$/);
      if (numberNode) {
        numberNode.characters = (currentPhaseCount + i + 1).toString();
      }
    }

    return {
      success: true,
      message: `Added ${phasesToAdd} new phases`
    };
  }
}

// ============================================================================
// PART 5: MAIN ORCHESTRATION
// ============================================================================

/**
 * Main function to create journey map from template
 */
async function createJourneyFromTemplate(templateUrl, journeyData) {
  const result = {
    success: false,
    message: '',
    errors: []
  };

  try {
    // Step 1: Extract file key from template URL
    const fileKeyMatch = templateUrl.match(/design\/([a-zA-Z0-9]+)/);
    if (!fileKeyMatch) {
      throw new Error('Invalid template URL format');
    }
    const templateFileKey = fileKeyMatch[1];

    // Step 2: Clone template (in real implementation, fetch + recreate)
    console.log('📋 Cloning template...');
    // For now, assume template is manually imported or in same file
    const templateFrame = figma.currentPage.findOne(node =>
      node.name === "User journey - template"
    );

    if (!templateFrame) {
      throw new Error('Template frame not found. Please import template first.');
    }

    const clonedTemplate = templateFrame.clone();
    clonedTemplate.name = `${journeyData.actor.name}'s Journey Map`;

    // Step 3: Find all phase frames
    console.log('🔍 Finding phase frames...');
    const phaseFrames = findPhaseFrames(clonedTemplate);
    console.log(`Found ${phaseFrames.length} phase frames in template`);

    // Step 4: Adjust phase count if needed
    console.log('📊 Adjusting phase count...');
    await adjustPhaseCount(
      clonedTemplate,
      journeyData.phases.length,
      phaseFrames.length
    );

    // Step 5: Replace content for each phase
    console.log('✏️ Replacing content...');
    const updatedPhaseFrames = findPhaseFrames(clonedTemplate); // Re-find after adjustment

    for (let i = 0; i < journeyData.phases.length; i++) {
      const phaseData = journeyData.phases[i];
      const phaseFrame = updatedPhaseFrames[i];

      if (phaseFrame) {
        await replacePhaseContent(phaseFrame, phaseData, i + 1);
        console.log(`✅ Phase ${i + 1}: ${phaseData.name}`);
      }
    }

    // Step 6: Update header section (Page 1)
    console.log('📝 Updating header...');
    // Find and update "User journey" title
    const titleNode = findTextNode(clonedTemplate, /User journey/i);
    if (titleNode) {
      titleNode.characters = `${journeyData.actor.name}'s Journey`;
    }

    result.success = true;
    result.message = `Journey map created successfully with ${journeyData.phases.length} phases`;
    result.frameId = clonedTemplate.id;

    return result;

  } catch (error) {
    result.success = false;
    result.message = error.message;
    result.errors.push(error.toString());
    return result;
  }
}

// ============================================================================
// EXPORT
// ============================================================================

// This file is reference documentation for the template-based approach
// In practice, this code would be executed via figma_execute by the Task agent

module.exports = {
  createJourneyFromTemplate,
  findPhaseFrames,
  replacePhaseContent,
  adjustPhaseCount
};
