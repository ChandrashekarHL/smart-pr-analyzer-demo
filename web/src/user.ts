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
  if (!user) {
    return "guest";
  }
  return user.name.trim() || `user-${user.id}`;
}

export function avatarOrDefault(user: User): string {
  // Profiles imported from the old system may have empty strings.
  if (user.profile?.avatarUrl === "") {
    return "/static/default-avatar.png";
  }
  return user.profile?.avatarUrl ?? "/static/default-avatar.png";
}
