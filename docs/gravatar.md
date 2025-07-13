TITLE: Basic React Hook Usage for Gravatar Hovercards
DESCRIPTION: This snippet demonstrates the fundamental usage of the `useHovercards` React hook. It shows how to import the hook and styles, initialize the hook, and use the `attach` method within a `useEffect` hook to enable hovercards on elements within a referenced container after the component mounts. It includes examples for both `<img>` tags with Gravatar URLs and elements with the `data-gravatar-hash` attribute.
SOURCE: https://github.com/automattic/gravatar/blob/trunk/web/packages/hovercards/README.md#_snippet_16

LANGUAGE: jsx
CODE:
```
import { useEffect, useRef } from 'react';
// Import the React hook
import { useHovercards } from '@gravatar-com/hovercards/react';
// Import the hovercard styles
import '@gravatar-com/hovercards/dist/style.css';

function App() {
    const { attach } = useHovercards( { /* Options */ } );
    const containerRef = useRef();

    useEffect( () => {
        if ( containerRef.current ) {
            attach( containerRef.current );
        }
    }, [ attach ] );

    return (
        <div ref={ containerRef }>
            { /* Work with Gravatar images */ }
            <img src="https://www.gravatar.com/avatar/<HASHED_EMAIL_ADDRESS>" alt="Gravatar Image" />
            <img src="https://www.gravatar.com/avatar/<HASHED_EMAIL_ADDRESS>" alt="Gravatar Image" />

            { /* Work with elements having `data-gravatar-hash` attribute */ }
            <div data-gravatar-hash="<HASHED_EMAIL_ADDRESS>">@Meow</div>
            <div data-gravatar-hash="<HASHED_EMAIL_ADDRESS>">@Woof</div>
        </div>
    );
}
```

----------------------------------------

TITLE: Creating a Custom React Component with useHovercards
DESCRIPTION: This example illustrates how to build a reusable React component (`Avatar`) that utilizes the `useHovercards` hook internally. The component takes an email address, calculates its SHA-256 hash, constructs the Gravatar URL, and uses `useRef` and `useEffect` to attach hovercard functionality specifically to the rendered `<img>` element, providing a convenient way to display hovercard-enabled avatars.
SOURCE: https://github.com/automattic/gravatar/blob/trunk/web/packages/hovercards/README.md#_snippet_17

LANGUAGE: jsx
CODE:
```
import sha256 from 'js-sha256';
import { useEffect, useRef } from 'react';
import { useHovercards } from '@gravatar-com/hovercards/react';
import '@gravatar-com/hovercards/dist/style.css';

// A custom Avatar component for convenience
function Avatar( { email } ) {
    const { attach } = useHovercards();
    const imgRef = useRef();

    useEffect( () => {
        if ( imgRef.current ) {
            attach( imgRef.current );
        }
    }, [ attach ] );

    return (
        <img ref={ imgRef } src={ `https://www.gravatar.com/avatar/${ sha256( email ) }` } alt="Gravatar Image" />
    );
}
```

----------------------------------------

TITLE: avatarUrl Method Signature
DESCRIPTION: The signature for the avatarUrl function, showing its parameters: email (string) and optional options (GravatarOptions).
SOURCE: https://github.com/automattic/gravatar/blob/trunk/web/packages/url-utils/README.md#_snippet_7

LANGUAGE: js
CODE:
```
avatarUrl(email, options: GravatarOptions)
```

----------------------------------------

TITLE: Usage with ES Modules
DESCRIPTION: Import and use the avatarUrl and profileUrl functions directly from the package using ES module syntax.
SOURCE: https://github.com/automattic/gravatar/blob/trunk/web/packages/url-utils/README.md#_snippet_2

LANGUAGE: js
CODE:
```
import { avatarUrl, profileUrl } from '@gravatar-com/url-utils';

avatarUrl( 'sara@example.com', { size: 500 } );
// https://www.gravatar.com/avatar/259b65833bbadfd58ee66dde290489a6e51518339de4886d2331027751f0913a?size=500

profileUrl( 'sara@example.com' );
// https://www.gravatar.com/259b65833bbadfd58ee66dde290489a6e51518339de4886d2331027751f0913a
```

----------------------------------------

TITLE: Using Gravatar Hovercards React Component
DESCRIPTION: Basic example demonstrating how to import and use the `Hovercards` React component to wrap elements (like `<img>` or `<div>` with `data-gravatar-hash`) that should trigger hovercards. Requires importing the component and the CSS styles.
SOURCE: https://github.com/automattic/gravatar/blob/trunk/web/packages/hovercards/README.md#_snippet_14

LANGUAGE: jsx
CODE:
```
// Import the React component
import { Hovercards } from '@gravatar-com/hovercards/react';
// Import the hovercard styles
import '@gravatar-com/hovercards/dist/style.css';

function App() {
    // ...

    return (
        <Hovercards>
            { /* Work with Gravatar images */ }
            <img src="https://www.gravatar.com/avatar/<HASHED_EMAIL_ADDRESS>" alt="Gravatar Image" />
            <img src="https://www.gravatar.com/avatar/<HASHED_EMAIL_ADDRESS>" alt="Gravatar Image" />

            { /* Work with elements having `data-gravatar-hash` attribute */ }
            <div data-gravatar-hash="<HASHED_EMAIL_ADDRESS>">@Meow</div>
            <div data-gravatar-hash="<HASHED_EMAIL_ADDRESS>">@Woof</div>
        </Hovercards>
    );
}
```

----------------------------------------

TITLE: Including Gravatar Images in HTML
DESCRIPTION: Demonstrates how to embed Gravatar images in an HTML page using <img> tags. The src attribute points to the Gravatar URL, including the hashed email address. Shows examples with and without URL parameters for size, default image, and rating.
SOURCE: https://github.com/automattic/gravatar/blob/trunk/web/packages/hovercards/README.md#_snippet_5

LANGUAGE: html
CODE:
```
<div id="container">
    <img id="avatar-1" src="https://www.gravatar.com/avatar/<HASHED_EMAIL_ADDRESS>" alt="Gravatar Image">
    <img id="avatar-2" src="https://www.gravatar.com/avatar/<HASHED_EMAIL_ADDRESS>" alt="Gravatar Image">

    <!-- Image URL with specified parameters -->
    <img id="avatar-3" src="https://www.gravatar.com/avatar/<HASHED_EMAIL_ADDRESS>?s=250&d=retro&r=pg" alt="Gravatar Image">
</div>
```

----------------------------------------

TITLE: Installing Gravatar Hovercards with React Dependencies using NPM
DESCRIPTION: Command to install the Gravatar Hovercards library along with React and ReactDOM dependencies using npm, required for React integration.
SOURCE: https://github.com/automattic/gravatar/blob/trunk/web/packages/hovercards/README.md#_snippet_2

LANGUAGE: Bash
CODE:
```
npm install add react react-dom @gravatar-com/hovercards
```

----------------------------------------

TITLE: Install with npm
DESCRIPTION: Add the @gravatar-com/url-utils package to your project using the npm package manager.
SOURCE: https://github.com/automattic/gravatar/blob/trunk/web/packages/url-utils/README.md#_snippet_0

LANGUAGE: sh
CODE:
```
npm install --save @gravatar-com/url-utils
```

----------------------------------------

TITLE: Installing Gravatar Hovercards with NPM
DESCRIPTION: Command to install the Gravatar Hovercards library using the npm package manager.
SOURCE: https://github.com/automattic/gravatar/blob/trunk/web/packages/hovercards/README.md#_snippet_0

LANGUAGE: Bash
CODE:
```
npm install @gravatar-com/hovercards
```

----------------------------------------

TITLE: Install Gravatar Quick Editor with NPM - Bash
DESCRIPTION: Installs the Gravatar Quick Editor library using the npm package manager. This command adds the package as a dependency to your project.
SOURCE: https://github.com/automattic/gravatar/blob/trunk/web/packages/quick-editor/README.md#_snippet_0

LANGUAGE: Bash
CODE:
```
npm install @gravatar-com/quick-editor
```

----------------------------------------

TITLE: avatarUrl Examples
DESCRIPTION: Demonstrates various ways to use the avatarUrl function, including specifying size and default image options.
SOURCE: https://github.com/automattic/gravatar/blob/trunk/web/packages/url-utils/README.md#_snippet_3

LANGUAGE: ts
CODE:
```
avatarUrl( 'sara@example.com' );
// https://www.gravatar.com/avatar/259b65833bbadfd58ee66dde290489a6e51518339de4886d2331027751f0913a

avatarUrl( 'sara@example.com', { size: 500 } );
// https://www.gravatar.com/avatar/259b65833bbadfd58ee66dde290489a6e51518339de4886d2331027751f0913a?size=500

avatarUrl( 'sara@example.com', { size: 500, default: GravatarDefault.Robohash } );
// https://www.gravatar.com/avatar/259b65833bbadfd58ee66dde290489a6e51518339de4886d2331027751f0913a?size=500&default=robohash

avatarUrl( 'sara@example.com', { size: 500, default: 'robohash' } );
// https://www.gravatar.com/avatar/259b65833bbadfd58ee66dde290489a6e51518339de4886d2331027751f0913a?size=500&default=robohash
```

----------------------------------------

TITLE: profileUrl Examples
DESCRIPTION: Shows examples of generating Gravatar profile URLs, including specifying the desired format like QR code.
SOURCE: https://github.com/automattic/gravatar/blob/trunk/web/packages/url-utils/README.md#_snippet_4

LANGUAGE: ts
CODE:
```
profileUrl( 'sara@example.com' );
// https://www.gravatar.com/259b65833bbadfd58ee66dde290489a6e51518339de4886d2331027751f0913a

profileUrl( 'sara@example.com', GravatarFormat.QR );
// https://www.gravatar.com/259b65833bbadfd58ee66dde290489a6e51518339de4886d2331027751f0913a.qr

profileUrl( 'sara@example.com', 'qr');
// https://www.gravatar.com/259b65833bbadfd58ee66dde290489a6e51518339de4886d2331027751f0913a.qr
```

----------------------------------------

TITLE: Install Gravatar Quick Editor with Yarn - Bash
DESCRIPTION: Installs the Gravatar Quick Editor library using the yarn package manager. This command adds the package as a dependency to your project.
SOURCE: https://github.com/automattic/gravatar/blob/trunk/web/packages/quick-editor/README.md#_snippet_1

LANGUAGE: Bash
CODE:
```
yarn add @gravatar-com/quick-editor
```

----------------------------------------

TITLE: Installing Gravatar Hovercards with Yarn
DESCRIPTION: Command to install the Gravatar Hovercards library using the Yarn package manager.
SOURCE: https://github.com/automattic/gravatar/blob/trunk/web/packages/hovercards/README.md#_snippet_1

LANGUAGE: Bash
CODE:
```
yarn add @gravatar-com/hovercards
```

----------------------------------------

TITLE: Initialize GravatarQuickEditor - TypeScript
DESCRIPTION: Initializes the simplified GravatarQuickEditor class. This class automatically sets up event handlers to open the editor popup and update specified avatar elements on the page based on the provided options.
SOURCE: https://github.com/automattic/gravatar/blob/trunk/web/packages/quick-editor/README.md#_snippet_4

LANGUAGE: TypeScript
CODE:
```
import { GravatarQuickEditor } from '@gravatar-com/quick-editor';

document.addEventListener( 'DOMContentLoaded', () => {
  new GravatarQuickEditor( {
    email: 'user@example.com',
    editorTriggerSelector: '#edit-profile',
    avatarSelector: '#gravatar-avatar',
    scope: [ 'avatars' ],
  } );
} );
```

----------------------------------------

TITLE: Using data-gravatar-hash Attribute in HTML
DESCRIPTION: Demonstrates using the data-gravatar-hash attribute on arbitrary HTML elements to associate a Gravatar hash. This allows hovercards to be attached to elements other than <img> tags. Shows examples with and without URL parameters appended to the hash value.
SOURCE: https://github.com/automattic/gravatar/blob/trunk/web/packages/hovercards/README.md#_snippet_7

LANGUAGE: html
CODE:
```
<div id="container">
    <div id="ref-1" data-gravatar-hash="<HASHED_EMAIL_ADDRESS>">@Meow</div>
    <div id="ref-2" data-gravatar-hash="<HASHED_EMAIL_ADDRESS>">@Woof</div>

    <!-- A hash with specified parameters -->
    <div id="ref-3" data-gravatar-hash="<HASHED_EMAIL_ADDRESS>?s=250&d=retro&r=pg">@Haha</div>
</div>
```

----------------------------------------

TITLE: Example React Component
DESCRIPTION: A TypeScript React component demonstrating how to integrate the avatarUrl function to display a user's Gravatar image.
SOURCE: https://github.com/automattic/gravatar/blob/trunk/web/packages/url-utils/README.md#_snippet_5

LANGUAGE: typescript
CODE:
```
import { avatarUrl } from '@gravatar-com/url-utils';

interface GravatarProps {
	email: string;
	size?: number;
}

const Gravatar = ( { email, size }: GravatarProps ) => {
	return (
		<img
			src={ avatarUrl( email, size ? { size: size } : null ) }
			alt="User Avatar"
			width={ size }
			height={ size }
		/>
	);
};

export default Gravatar;
```

----------------------------------------

TITLE: Access Gravatar Quick Editor Global Object - JavaScript
DESCRIPTION: Demonstrates how to access the Gravatar Quick Editor library as a global variable named 'Gravatar' after importing it via the UNPKG CDN in an HTML script tag.
SOURCE: https://github.com/automattic/gravatar/blob/trunk/web/packages/quick-editor/README.md#_snippet_3

LANGUAGE: JavaScript
CODE:
```
console.log( Gravatar );
```

----------------------------------------

TITLE: Attaching Hovercards to data-gravatar-hash Elements (JS)
DESCRIPTION: Initializes the Gravatar Hovercards library and attaches hovercard behavior to elements with the data-gravatar-hash attribute. Shows how to attach to a single element, all elements within a container, or all elements on the page. Requires importing the library and its styles.
SOURCE: https://github.com/automattic/gravatar/blob/trunk/web/packages/hovercards/README.md#_snippet_8

LANGUAGE: javascript
CODE:
```
import { Hovercards } from '@gravatar-com/hovercards';
import '@gravatar-com/hovercards/dist/styles.css';

document.addEventListener( 'DOMContentLoaded', () => {
    // Start the hovercards feature with your preferred settings
    const hovercards = new Hovercards( { /* Options */ } );

    // Attach hovercards on a specific image
    hovercards.attach( document.getElementById( 'ref-1' ) );

    // Attach to all images within a container
    hovercards.attach( document.getElementById( 'container' ) );

    // Attach to all images on the page
    hovercards.attach( document.body );
} );
```

----------------------------------------

TITLE: Attaching Hovercards to Gravatar Images (JS)
DESCRIPTION: Initializes the Gravatar Hovercards library and attaches hovercard behavior to elements containing Gravatar images. Shows how to attach to a single element, all elements within a container, or all elements on the page. Includes an example of excluding elements using ignoreSelector. Requires importing the library and its styles.
SOURCE: https://github.com/automattic/gravatar/blob/trunk/web/packages/hovercards/README.md#_snippet_6

LANGUAGE: javascript
CODE:
```
import { Hovercards } from '@gravatar-com/hovercards';
// Import the hovercard styles
import '@gravatar-com/hovercards/dist/style.css';

document.addEventListener( 'DOMContentLoaded', () => {
    // Start the hovercards feature with your preferred settings
    const hovercards = new Hovercards( { /* Options */ } );

    // Make hovercards work on a specific Gravatar image
    hovercards.attach( document.getElementById( 'avatar-1' ) );

    // Alternatively, make hovercards work on all Gravatar images within a specific container
    hovercards.attach( document.getElementById( 'container' ) );

    // If you want hovercards on all Gravatar images across the entire page, use `document.body` as the target
    hovercards.attach( document.body );

    // You can exclude certain Gravatar images from hovercards by using `ignoreSelector`
    hovercards.attach( document.body, { ignoreSelector: '.ignore img[src*="gravatar.com/avatar/"]' } );
} );
```

----------------------------------------

TITLE: Using the React Component
DESCRIPTION: Examples showing how to use the Gravatar React component in JSX with and without the size prop.
SOURCE: https://github.com/automattic/gravatar/blob/trunk/web/packages/url-utils/README.md#_snippet_6

LANGUAGE: html
CODE:
```
<Gravatar email="sara@example.com" />
<Gravatar email="sara@example.com" size={500} />
```

----------------------------------------

TITLE: Install with UNPKG
DESCRIPTION: Import the library using a script tag from UNPKG for use in vanilla JavaScript environments and access it via the global GravatarUrlUtils object.
SOURCE: https://github.com/automattic/gravatar/blob/trunk/web/packages/url-utils/README.md#_snippet_1

LANGUAGE: html
CODE:
```
<!-- Import the url-utils library -->
<script src="https://unpkg.com/@gravatar-com/url-utils@x.x.x" defer></script>

<script>
  // The library is accessible as a global variable "GravatarUrlUtils"
	console.log( GravatarUrlUtils.avatarUrl('example@example.com') );
</script>
```

----------------------------------------

TITLE: Create Static Gravatar Hovercard Element (JavaScript)
DESCRIPTION: This JavaScript example demonstrates how to use the static createHovercard method from the @gravatar-com/hovercards library to generate an HTMLDivElement representing a Gravatar hovercard. It requires a ProfileData object and can accept optional configuration for additional styling or internationalization.
SOURCE: https://github.com/automattic/gravatar/blob/trunk/web/packages/hovercards/README.md#_snippet_11

LANGUAGE: JavaScript
CODE:
```
import { Hovercards } from '@gravatar-com/hovercards';

const hovercard = Hovercards.createHovercard( {
    hash: '...',
    avatarUrl: '...',
    profileUrl: '...',
    displayName: '...',
    description: '...',
    location: '...',
    jobTitle: '...',
    company: '...',
    verifiedAccounts = [ {
        label: '...',
        icon: '...',
        url: '...',
        type: '...',
    } ],
} );

document.getElementById( 'container' ).appendChild( hovercard );
```

----------------------------------------

TITLE: Attaching Gravatar Hovercards React Component to Element
DESCRIPTION: Example showing how to use the `attach` prop on the `Hovercards` React component to apply hovercard functionality to a specific target element, such as the entire document body, instead of wrapping child elements.
SOURCE: https://github.com/automattic/gravatar/blob/trunk/web/packages/hovercards/README.md#_snippet_15

LANGUAGE: jsx
CODE:
```
import { Hovercards } from '@gravatar-com/hovercards/react';
import '@gravatar-com/hovercards/dist/style.css';

function App() {
    // ...

    return (
        <>
            <div>
                <img src="https://www.gravatar.com/avatar/<HASHED_EMAIL_ADDRESS>" alt="Gravatar Image" />
                <img src="https://www.gravatar.com/avatar/<HASHED_EMAIL_ADDRESS>" alt="Gravatar Image" />
                <img src="https://www.gravatar.com/avatar/<HASHED_EMAIL_ADDRESS>" alt="Gravatar Image" />
            </div>
            { /* Attach hovercards to the entire page */ }
            <Hovercards attach={ document.body } />
        </>
    );
}
```

----------------------------------------

TITLE: Importing Gravatar Hovercards via UNPKG CDN (Vanilla JS)
DESCRIPTION: HTML snippet demonstrating how to include the Gravatar Hovercards library and its styles directly from the UNPKG CDN for use in vanilla JavaScript projects. It shows linking the CSS and JS files and accessing the library globally.
SOURCE: https://github.com/automattic/gravatar/blob/trunk/web/packages/hovercards/README.md#_snippet_3

LANGUAGE: HTML
CODE:
```
<!-- Import the hovercard styles -->
<link rel="stylesheet" href="https://unpkg.com/@gravatar-com/hovercards@x.x.x/dist/style.css">

<!-- Import the hovercards library -->
<script src="https://unpkg.com/@gravatar-com/hovercards@x.x.x" defer></script>

<script>
  // The library is accessible as a global variable
  console.log( Gravatar );
</script>
```

----------------------------------------

TITLE: Create Gravatar Hovercard Skeleton Element (JavaScript)
DESCRIPTION: This JavaScript example shows how to use the static createHovercardSkeleton method to create an HTMLDivElement that serves as a placeholder or loading state for a Gravatar hovercard. It's useful for displaying while profile data is being fetched asynchronously.
SOURCE: https://github.com/automattic/gravatar/blob/trunk/web/packages/hovercards/README.md#_snippet_12

LANGUAGE: JavaScript
CODE:
```
import { Hovercards } from '@gravatar-com/hovercards';

const hovercardSkeleton = Hovercards.createHovercardSkeleton();

document.getElementById( 'container' ).appendChild( hovercardSkeleton );
```

----------------------------------------

TITLE: Importing Gravatar Hovercards via UNPKG CDN (React)
DESCRIPTION: HTML snippet demonstrating how to include the Gravatar Hovercards library and its styles directly from the UNPKG CDN for use in React projects. It requires React and ReactDOM to be imported first and then includes the React-specific UMD build.
SOURCE: https://github.com/automattic/gravatar/blob/trunk/web/packages/hovercards/README.md#_snippet_4

LANGUAGE: HTML
CODE:
```
<link rel="stylesheet" href="https://unpkg.com/@gravatar-com/hovercards@x.x.x/dist/style.css">

<!-- Ensure React and ReactDOM are imported before the library -->
<script src="https://unpkg.com/react@x.x.x" defer></script>
<script src="https://unpkg.com/react-dom@x.x.x" defer></script>
<!-- Import the React hovercards library -->
<script src="https://unpkg.com/@gravatar-com/hovercards@x.x.x/dist/index.react.umd.js" defer></script>

<script>
  console.log( Gravatar );
</script>
```

----------------------------------------

TITLE: Import Gravatar Quick Editor via UNPKG - HTML
DESCRIPTION: Includes the Gravatar Quick Editor library in an HTML page directly from the UNPKG CDN using a script tag. The 'defer' attribute ensures the script executes after the document is parsed.
SOURCE: https://github.com/automattic/gravatar/blob/trunk/web/packages/quick-editor/README.md#_snippet_2

LANGUAGE: HTML
CODE:
```
<!-- Import the library -->
<script src="https://unpkg.com/@gravatar-com/quick-editor@x.x.x" defer></script>
```

----------------------------------------

TITLE: Create Gravatar Hovercard Error Element (JavaScript)
DESCRIPTION: This JavaScript example demonstrates using the static createHovercardError method to generate an HTMLDivElement displaying an error message for a Gravatar hovercard. It requires the avatar URL and an error message, and can include optional parameters for styling or alternative text.
SOURCE: https://github.com/automattic/gravatar/blob/trunk/web/packages/hovercards/README.md#_snippet_13

LANGUAGE: JavaScript
CODE:
```
import { Hovercards } from '@gravatar-com/hovercards';

const hovercardError = Hovercards.createHovercardError( 'https://www.gravatar.com/avatar/<HASHED_EMAIL_ADDRESS>', 'Error message' );

document.getElementById( 'container' ).appendChild( hovercardError );
```

----------------------------------------

TITLE: Initialize and Use GravatarQuickEditorCore - TypeScript
DESCRIPTION: Initializes the advanced GravatarQuickEditorCore class. This class provides manual control over opening the editor and allows setting up custom callback functions for events like profile updates or editor opening.
SOURCE: https://github.com/automattic/gravatar/blob/trunk/web/packages/quick-editor/README.md#_snippet_5

LANGUAGE: TypeScript
CODE:
```
import { GravatarQuickEditorCore } from '@gravatar-com/quick-editor';

document.addEventListener( 'DOMContentLoaded', () => {
  const quickEditorCore = new GravatarQuickEditorCore( {
    email: 'user@example.com',
    scope: [ 'avatars', 'about' ],
    onProfileUpdated: () => {
      console.log( 'Profile updated!' );
    },
    onOpened: () => {
      console.log( 'Editor opened!' );
    },
  } );

  document.getElementById( 'edit-profile' ).addEventListener( 'click', () => {
    quickEditorCore.open();
  } );
} );
```

----------------------------------------

TITLE: Define Gravatar Profile Data Interface (TypeScript)
DESCRIPTION: This TypeScript interface defines the structure of the ProfileData object, which contains detailed information about a Gravatar profile. It includes properties like hash, avatar URL, display name, location, and optional fields like verified accounts and contact info.
SOURCE: https://github.com/automattic/gravatar/blob/trunk/web/packages/hovercards/README.md#_snippet_9

LANGUAGE: TypeScript
CODE:
```
interface ProfileData {
    hash: string;
    avatarUrl: string;
    profileUrl: string;
    displayName: string;
    location?: string;
    description?: string;
    jobTitle?: string;
    company?: string;
    headerImage?: string;
    backgroundColor?: string;
    verifiedAccounts?: Record< 'label' | 'icon' | 'url' | 'type', string >[];
    contactInfo?: ContactInfo;
    payments?: Payments;
}
```

----------------------------------------

TITLE: Providing Translations with the i18n Option
DESCRIPTION: This snippet shows the structure for providing custom translations using the `i18n` option available in the Gravatar Hovercards library. It is a simple JavaScript object where keys are the default English phrases used by the library and values are the desired translated strings, allowing customization of the text displayed in the hovercards.
SOURCE: https://github.com/automattic/gravatar/blob/trunk/web/packages/hovercards/README.md#_snippet_18

LANGUAGE: js
CODE:
```
{
  'Edit your profile →': 'Modifier votre profil →'
}
```

----------------------------------------

TITLE: QuickEditorOptions Type Definition - TypeScript
DESCRIPTION: Defines the structure and types for the configuration object used when initializing the GravatarQuickEditor class, including properties for email, selectors, scope, locale, and avatar refresh delay.
SOURCE: https://github.com/automattic/gravatar/blob/trunk/web/packages/quick-editor/README.md#_snippet_7

LANGUAGE: TypeScript
CODE:
```
type QuickEditorOptions = {
  email: string;
  editorTriggerSelector: string;
  avatarSelector?: string;
  scope?: Scope;
  locale?: string;
  avatarRefreshDelay?: number;
};
```

----------------------------------------

TITLE: Defining QuickEditorCoreOptions Type (Typescript)
DESCRIPTION: Defines the Typescript type for configuring the Gravatar Quick Editor. It is a partial type allowing optional configuration of the email, scope, locale, and callback functions for profile updates and editor opening.
SOURCE: https://github.com/automattic/gravatar/blob/trunk/web/packages/quick-editor/README.md#_snippet_9

LANGUAGE: typescript
CODE:
```
type QuickEditorCoreOptions = Partial< {
  email: string;
  scope: Scope;
  locale: string;
  onProfileUpdated: OnProfileUpdated;
  onOpened: OnOpened;
} >;
```

----------------------------------------

TITLE: Build Development Bundle npm Bash
DESCRIPTION: Builds the library in development mode, generating bundled files in the dist folder without optimization.
SOURCE: https://github.com/automattic/gravatar/blob/trunk/docs/CONTRIBUTING.md#_snippet_6

LANGUAGE: bash
CODE:
```
npm run build:dev
```

----------------------------------------

TITLE: Check Types TypeScript npm Bash
DESCRIPTION: Performs static type checking on the TypeScript code to catch type-related errors.
SOURCE: https://github.com/automattic/gravatar/blob/trunk/docs/CONTRIBUTING.md#_snippet_8

LANGUAGE: bash
CODE:
```
npm run type-check
```

----------------------------------------

TITLE: Define Gravatar Fetch Profile Error Interface (TypeScript)
DESCRIPTION: This TypeScript interface defines the structure of the FetchProfileError object, which is provided to the onFetchProfileFailure callback. It contains a numeric code and a string message describing the error that occurred during profile fetching.
SOURCE: https://github.com/automattic/gravatar/blob/trunk/web/packages/hovercards/README.md#_snippet_10

LANGUAGE: TypeScript
CODE:
```
interface FetchProfileError {
    code: number;
    message: string;
}
```

----------------------------------------

TITLE: profileUrl Method Signature
DESCRIPTION: The signature for the profileUrl function, showing its parameters: email (string) and optional format (GravatarFormat).
SOURCE: https://github.com/automattic/gravatar/blob/trunk/web/packages/url-utils/README.md#_snippet_8

LANGUAGE: js
CODE:
```
profileUrl(email, format: GravatarFormat)
```

----------------------------------------

TITLE: GravatarQuickEditorCore Constructor Signature - TypeScript
DESCRIPTION: Defines the constructor signature for the GravatarQuickEditorCore class, showing it accepts an options object of type QuickEditorCoreOptions.
SOURCE: https://github.com/automattic/gravatar/blob/trunk/web/packages/quick-editor/README.md#_snippet_8

LANGUAGE: TypeScript
CODE:
```
new GravatarQuickEditorCore(options: QuickEditorCoreOptions);
```

----------------------------------------

TITLE: GravatarQuickEditor Constructor Signature - TypeScript
DESCRIPTION: Defines the constructor signature for the GravatarQuickEditor class, indicating that it is initialized with an options object conforming to the QuickEditorOptions type.
SOURCE: https://github.com/automattic/gravatar/blob/trunk/web/packages/quick-editor/README.md#_snippet_6

LANGUAGE: TypeScript
CODE:
```
new GravatarQuickEditor(options: QuickEditorOptions);
```

----------------------------------------

TITLE: Lint Markdown npm Bash
DESCRIPTION: Lints the Markdown documentation files to ensure consistent formatting and style.
SOURCE: https://github.com/automattic/gravatar/blob/trunk/docs/CONTRIBUTING.md#_snippet_11

LANGUAGE: bash
CODE:
```
npm run lint:md:docs
```

----------------------------------------

TITLE: Install Dependencies npm Bash
DESCRIPTION: Installs the project dependencies using npm. Ensure your Node version meets the minimum requirement specified in package.json.
SOURCE: https://github.com/automattic/gravatar/blob/trunk/docs/CONTRIBUTING.md#_snippet_0

LANGUAGE: bash
CODE:
```
npm install
```

----------------------------------------

TITLE: Lint JavaScript/TypeScript npm Bash
DESCRIPTION: Lints the JavaScript and TypeScript code to enforce code quality and style rules.
SOURCE: https://github.com/automattic/gravatar/blob/trunk/docs/CONTRIBUTING.md#_snippet_9

LANGUAGE: bash
CODE:
```
npm run lint:js
```

----------------------------------------

TITLE: Clean Distribution Folder npm Bash
DESCRIPTION: Removes the generated distribution folder (dist) containing the bundled files.
SOURCE: https://github.com/automattic/gravatar/blob/trunk/docs/CONTRIBUTING.md#_snippet_13

LANGUAGE: bash
CODE:
```
npm run clean:dist
```

----------------------------------------

TITLE: Run Gravatar CLI - Get Avatar (sh)
DESCRIPTION: Executes the Gravatar command-line tool to fetch the avatar URL for a given email address using `npm exec`.
SOURCE: https://github.com/automattic/gravatar/blob/trunk/web/packages/url-utils/README.md#_snippet_11

LANGUAGE: sh
CODE:
```
npm exec -- gravatar --avatar sara@example.com
```

----------------------------------------

TITLE: Run Gravatar CLI - Get Profile (sh)
DESCRIPTION: Executes the Gravatar command-line tool to fetch the profile information for a given email address using `npm exec`.
SOURCE: https://github.com/automattic/gravatar/blob/trunk/web/packages/url-utils/README.md#_snippet_12

LANGUAGE: sh
CODE:
```
npm exec -- gravatar --profile sara@example.com
```

----------------------------------------

TITLE: Project Directory Structure
DESCRIPTION: An overview of the main directories and files within the project repository.
SOURCE: https://github.com/automattic/gravatar/blob/trunk/web/packages/url-utils/README.md#_snippet_9

LANGUAGE: sh
CODE:
```
.
├── README.md               # You are here
├── dist                    # Output files (js and types)
├── lint-staged.config.js
├── package.json
├── src                     # Code
│   ├── cli.ts              # Very basic cli tool
│   └── index.ts            # The main library
├── tests                   # Unit tests, you should proabaly start here
│   └── index.test.ts
├── webpack                 # Webpack config
├── tsconfig.json
└── babel.config.ts
```

----------------------------------------

TITLE: Start Development Server npm Bash
DESCRIPTION: Starts a local server to test the library in development mode, allowing you to test code changes in the playground directory.
SOURCE: https://github.com/automattic/gravatar/blob/trunk/docs/CONTRIBUTING.md#_snippet_3

LANGUAGE: bash
CODE:
```
npm run start
```

----------------------------------------

TITLE: Build and Watch Development Bundle npm Bash
DESCRIPTION: Builds the library in development mode and watches for file changes, automatically recompiling upon modification.
SOURCE: https://github.com/automattic/gravatar/blob/trunk/docs/CONTRIBUTING.md#_snippet_2

LANGUAGE: bash
CODE:
```
npm run build:watch
```

----------------------------------------

TITLE: Format Code npm Bash
DESCRIPTION: Formats the code according to the project's style guidelines using the configured formatting tool.
SOURCE: https://github.com/automattic/gravatar/blob/trunk/docs/CONTRIBUTING.md#_snippet_7

LANGUAGE: bash
CODE:
```
npm run format
```

----------------------------------------

TITLE: Fix Linting Errors npm Bash
DESCRIPTION: Automatically fixes linting errors for a specific type (e.g., js, style, md:docs) using the configured linters.
SOURCE: https://github.com/automattic/gravatar/blob/trunk/docs/CONTRIBUTING.md#_snippet_4

LANGUAGE: bash
CODE:
```
npm run lint:<TYPE> --fix
```

----------------------------------------

TITLE: Build Production Bundle npm Bash
DESCRIPTION: Builds the library in production mode, generating optimized bundled files in the dist folder.
SOURCE: https://github.com/automattic/gravatar/blob/trunk/docs/CONTRIBUTING.md#_snippet_5

LANGUAGE: bash
CODE:
```
npm run build
```

----------------------------------------

TITLE: Run Gravatar Tests (sh)
DESCRIPTION: Executes the project's test suite using the configured npm script.
SOURCE: https://github.com/automattic/gravatar/blob/trunk/web/packages/url-utils/README.md#_snippet_13

LANGUAGE: sh
CODE:
```
npm run test
```

----------------------------------------

TITLE: Lint Sass/CSS npm Bash
DESCRIPTION: Lints the Sass and CSS code to enforce style guidelines and catch potential issues.
SOURCE: https://github.com/automattic/gravatar/blob/trunk/docs/CONTRIBUTING.md#_snippet_10

LANGUAGE: bash
CODE:
```
npm run lint:style
```

----------------------------------------

TITLE: Build Gravatar Project (sh)
DESCRIPTION: Builds the project's JavaScript files from the TypeScript source code using the configured npm script.
SOURCE: https://github.com/automattic/gravatar/blob/trunk/web/packages/url-utils/README.md#_snippet_10

LANGUAGE: sh
CODE:
```
npm run build
```

----------------------------------------

TITLE: Run All Linters npm Bash
DESCRIPTION: Executes all configured linters (JavaScript/TypeScript, Sass/CSS, Markdown) to check the entire codebase.
SOURCE: https://github.com/automattic/gravatar/blob/trunk/docs/CONTRIBUTING.md#_snippet_12

LANGUAGE: bash
CODE:
```
npm run lint
```

----------------------------------------

TITLE: Clean Release Folder npm Bash
DESCRIPTION: Removes the generated release folder (release).
SOURCE: https://github.com/automattic/gravatar/blob/trunk/docs/CONTRIBUTING.md#_snippet_14

LANGUAGE: bash
CODE:
```
npm run clean:release
```

----------------------------------------

TITLE: Clean All Generated Folders npm Bash
DESCRIPTION: Removes all generated folders, including dist and release.
SOURCE: https://github.com/automattic/gravatar/blob/trunk/docs/CONTRIBUTING.md#_snippet_15

LANGUAGE: bash
CODE:
```
npm run clean
```

----------------------------------------

TITLE: Navigate to Package Directory Bash
DESCRIPTION: Changes the current directory to the specific package you are working on within the web/packages folder.
SOURCE: https://github.com/automattic/gravatar/blob/trunk/docs/CONTRIBUTING.md#_snippet_1

LANGUAGE: bash
CODE:
```
cd web/packages/[package-name]
```

----------------------------------------

TITLE: Create New Release npm Bash
DESCRIPTION: Executes the script to create a new release of the library.
SOURCE: https://github.com/automattic/gravatar/blob/trunk/docs/CONTRIBUTING.md#_snippet_16

LANGUAGE: bash
CODE:
```
npm run release
```
