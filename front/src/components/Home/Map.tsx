'use client';

import { GoogleMap, Marker, useJsApiLoader } from '@react-google-maps/api';
import { useTheme } from 'next-themes';
import { memo } from 'react';

const MapContainer = ({
  className,
  initialCenter,
}: {
  className: string;
  initialCenter: google.maps.LatLng | google.maps.LatLngLiteral;
}) => {
  const { resolvedTheme } = useTheme();
  const { isLoaded } = useJsApiLoader({
    id: 'google-map-script',
    googleMapsApiKey: process.env.NEXT_PUBLIC_GCP_MAP_API_KEY || '',
  });

  return isLoaded ? (
    <GoogleMap
      mapContainerClassName={className}
      center={initialCenter}
      zoom={12}
      options={{
        styles: resolvedTheme === 'dark' ? mapStylesDark : mapStylesLight,
        scrollwheel: false,
        keyboardShortcuts: false,
        disableDoubleClickZoom: true,
        zoomControl: false,
        mapTypeControl: false,
        scaleControl: false,
        streetViewControl: false,
        panControl: false,
        rotateControl: false,
        fullscreenControl: false,
      }}
    >
      <Marker position={initialCenter} />
    </GoogleMap>
  ) : (
    <></>
  );
};

export const Map = memo(MapContainer);

const mapStylesLight = [
  {
    featureType: 'landscape.natural',
    elementType: 'geometry.fill',
    stylers: [
      {
        visibility: 'on',
      },
      {
        color: '#eaeaea',
      },
    ],
  },
  {
    featureType: 'poi',
    elementType: 'geometry.fill',
    stylers: [
      {
        visibility: 'on',
      },
      {
        color: '#cccccc',
      },
    ],
  },
  {
    featureType: 'poi',
    elementType: 'labels',
    stylers: [
      {
        visibility: 'off',
      },
    ],
  },
  {
    featureType: 'road',
    elementType: 'geometry',
    stylers: [
      {
        lightness: 100,
      },
      {
        visibility: 'simplified',
      },
    ],
  },
  {
    featureType: 'road',
    elementType: 'labels',
    stylers: [
      {
        visibility: 'off',
      },
    ],
  },
  {
    featureType: 'transit.line',
    elementType: 'geometry',
    stylers: [
      {
        visibility: 'on',
      },
      {
        lightness: 700,
      },
    ],
  },
  {
    featureType: 'water',
    elementType: 'all',
    stylers: [
      {
        color: '#63B7FF',
      },
    ],
  },
];

const mapStylesDark = [
  {
    featureType: 'landscape.natural',
    elementType: 'geometry.fill',
    stylers: [
      {
        visibility: 'on',
      },
      {
        color: '#eaeaea',
      },
    ],
  },
  {
    featureType: 'poi',
    elementType: 'geometry.fill',
    stylers: [
      {
        visibility: 'on',
      },
      {
        color: '#cccccc',
      },
    ],
  },
  {
    featureType: 'poi',
    elementType: 'labels',
    stylers: [
      {
        visibility: 'off',
      },
    ],
  },
  {
    featureType: 'road',
    elementType: 'geometry',
    stylers: [
      {
        lightness: 100,
      },
      {
        visibility: 'simplified',
      },
    ],
  },
  {
    featureType: 'road',
    elementType: 'labels',
    stylers: [
      {
        visibility: 'off',
      },
    ],
  },
  {
    featureType: 'transit.line',
    elementType: 'geometry',
    stylers: [
      {
        visibility: 'on',
      },
      {
        lightness: 700,
      },
    ],
  },
  {
    featureType: 'water',
    elementType: 'all',
    stylers: [
      {
        color: '#000000',
      },
    ],
  },
];
