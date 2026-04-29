---
name: The Executive Portfolio
colors:
  surface: '#051424'
  surface-dim: '#051424'
  surface-bright: '#2c3a4c'
  surface-container-lowest: '#010f1f'
  surface-container-low: '#0d1c2d'
  surface-container: '#122131'
  surface-container-high: '#1c2b3c'
  surface-container-highest: '#273647'
  on-surface: '#d4e4fa'
  on-surface-variant: '#d0c5af'
  inverse-surface: '#d4e4fa'
  inverse-on-surface: '#233143'
  outline: '#99907c'
  outline-variant: '#4d4635'
  surface-tint: '#e9c349'
  primary: '#f2ca50'
  on-primary: '#3c2f00'
  primary-container: '#d4af37'
  on-primary-container: '#554300'
  inverse-primary: '#735c00'
  secondary: '#c8c6c8'
  on-secondary: '#313032'
  secondary-container: '#474649'
  on-secondary-container: '#b7b4b7'
  tertiary: '#d0cdd3'
  on-tertiary: '#303034'
  tertiary-container: '#b4b2b7'
  on-tertiary-container: '#454449'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffe088'
  primary-fixed-dim: '#e9c349'
  on-primary-fixed: '#241a00'
  on-primary-fixed-variant: '#574500'
  secondary-fixed: '#e5e1e4'
  secondary-fixed-dim: '#c8c6c8'
  on-secondary-fixed: '#1b1b1d'
  on-secondary-fixed-variant: '#474649'
  tertiary-fixed: '#e4e1e7'
  tertiary-fixed-dim: '#c8c5cb'
  on-tertiary-fixed: '#1b1b1f'
  on-tertiary-fixed-variant: '#47464b'
  background: '#051424'
  on-background: '#d4e4fa'
  surface-variant: '#273647'
typography:
  display-xl:
    fontFamily: Newsreader
    fontSize: 72px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  display-lg:
    fontFamily: Newsreader
    fontSize: 56px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Newsreader
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.3'
  headline-sm:
    fontFamily: Newsreader
    fontSize: 24px
    fontWeight: '400'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.7'
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  body-sm:
    fontFamily: Manrope
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.1em
  button:
    fontFamily: Manrope
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.0'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 8px
  section-gap: 120px
  container-max: 1200px
  gutter: 24px
  margin-mobile: 20px
  margin-desktop: 80px
---

## Brand & Style
This design system is built for high-stakes intellectual property and executive positioning. It treats digital space like a premium physical object—a limited-edition leather-bound volume translated into a futuristic interface. The brand personality is authoritative and rare, appealing to industry leaders who value substance over noise.

The visual style is a hybrid of **Minimalism** and **Glassmorphism**. By combining vast "white space" (rendered in deep charcoal) with translucent layers and metallic accents, the UI achieves a sense of depth and permanence. It avoids the fleeting trends of consumer apps in favor of a timeless, "published" aesthetic that suggests every word and interaction is intentional and vetted.

## Colors
The palette is rooted in the "Prestige Dark" aesthetic. The primary surface is an ultra-deep charcoal (#0E0E10), providing a canvas that feels more like an abyss than a screen. 

*   **Primary (Rich Gold):** Used sparingly for high-value calls to action, active states, and essential typographic highlights. It represents the "gilded edge" of a book.
*   **Secondary (Surface):** A slightly lighter charcoal (#1A1A1E) used for cards and nested containers to create structural separation.
*   **Typography:** We use Pure White (#FFFFFF) for primary headlines to ensure maximum readability against the dark background, and a muted Slate (#94A3B8) for secondary body text to reduce eye strain and establish a clear information hierarchy.

## Typography
The typography strategy mimics the layout of a high-end editorial publication. **Newsreader** provides the literary soul of the design system, used for large-scale storytelling and philosophical headers. Its serif structure conveys history and truth.

**Manrope** serves as the functional engine. It is utilized for body copy, technical data, and UI labels. The contrast between the organic, varying strokes of the serif and the geometric precision of the sans-serif creates the "futuristic yet grounded" tension requested. 

Key Rules:
- Display text should use italicization for emphasis, mirroring classic book emphasis.
- Line heights for body text are intentionally generous (1.6+) to simulate the airy feel of a luxury manuscript.

## Layout & Spacing
This design system utilizes a **Fixed Grid** model with a maximum content width of 1200px, centered on the viewport. This mimics the focused nature of a book page, ensuring that content does not become unreadably wide on ultra-wide monitors.

The spacing rhythm is "Atmospheric." We use large vertical gaps (120px+) between major sections to allow the user to mentally reset—this is the digital equivalent of turning a page. A 12-column grid is used for internal card layouts, typically following a 4-4-4 or 6-6 split to maintain symmetrical balance.

## Elevation & Depth
Depth in this design system is achieved through **Glassmorphism** and tonal layering. Rather than using aggressive drop shadows, we use:

1.  **Backdrop Blurs:** Secondary surfaces (cards, modals) use a 12px to 20px blur with a low-opacity black fill (approx 40-60%).
2.  **Gold Micro-Borders:** Interactive elements are defined by 1px solid borders. For primary elements, these borders use the Gold (#D4AF37) color. For neutral containers, use a subtle slate-gray border at 10% opacity.
3.  **Inner Glows:** To simulate the texture of high-end paper or metallic inlay, buttons feature a very soft top-down inner glow (white or gold at 5% opacity).
4.  **Ambient Shadows:** When a modal is present, use a large, diffused black shadow (0 20px 50px rgba(0,0,0,0.8)) to lift the element off the charcoal base.

## Shapes
The shape language is "Soft-Precision." We avoid the playful, bubbly nature of high roundedness (Pill-shaped) and the harsh, aggressive nature of sharp 0px corners. 

A uniform **0.25rem (4px)** radius is applied to standard UI elements like input fields and buttons. Larger containers like cards may use up to **0.5rem (8px)**. This slight rounding suggests modern manufacturing and luxury without losing the authoritative "square" feel of a traditional book.

## Components
### Buttons
- **Primary:** Solid gold background with black text. On hover, a subtle scale-up (1.02x) and an increase in outer glow brightness.
- **Secondary:** Transparent background with a 1px gold border and gold text.
- **Ghost:** Text-only with an underline that appears on hover, utilizing the serif font for a "literary link" feel.

### Cards
Cards should feel like "sheets" of glass. They feature a thin top-border in gold to signify importance. Content inside cards should be left-aligned with generous internal padding (32px or 40px).

### Input Fields
Inputs are minimal. They feature a 1px border on the bottom only by default, or a full 1px border with a 5% white fill. Focus states must transition the border color to gold.

### Chips & Badges
Small, all-caps labels using **Manrope**. They should have a dark background with a subtle border, never a solid bright color, to maintain the executive tone.

### Navigation
The navigation bar should be a "Floating Glass" element. It uses a high backdrop-filter blur and sits at the top of the viewport with a subtle bottom border.