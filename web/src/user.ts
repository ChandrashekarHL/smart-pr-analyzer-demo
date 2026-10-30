export interface Profile {
  avatarUrl?: string;
  bio?: string;
}

export interface User {
  id: number;
  name: string;
  profile?: Profile;
}

export function displayName(user: User): string {
  return user.name.trim() || `user-${user.id}`;
}

export function avatarOrDefault(user: User): string {
  return user.profile?.avatarUrl ?? "/static/default-avatar.png";
}
