import { Home } from '@/components/Home';

import db from './db.json';

export default function Page() {
  return <Home pages={db.pages} />;
}
